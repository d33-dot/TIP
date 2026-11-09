import os
import logging
import sqlite3
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import (
    ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, 
    InlineKeyboardButton, LabeledPrice, PreCheckoutQuery
)

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Токены (Замените на свои)
API_TOKEN = 'YOUR_BOT_TOKEN'
PROVIDER_TOKEN = 'YOUR_PROVIDER_TOKEN'
SUPPORT_ADMIN_ID = 123456789  # ID вашего аккаунта Telegram (или менеджера) для поддержки

bot = Bot(token=API_TOKEN)
dp = Dispatcher(storage=MemoryStorage())

# --- БАЗА ДАННЫХ ---
def init_db():
    conn = sqlite3.connect("shop.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            name TEXT,
            phone TEXT,
            address TEXT,
            email TEXT
        )
    """)
    conn.commit()
    conn.close()

def get_user(user_id):
    conn = sqlite3.connect("shop.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name, phone, address, email FROM users WHERE user_id = ?", (user_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return {"name": row[0], "phone": row[1], "address": row[2], "email": row[3]}
    return None

def save_user(user_id, data):
    conn = sqlite3.connect("shop.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT OR REPLACE INTO users (user_id, name, phone, address, email)
        VALUES (?, ?, ?, ?, ?)
    """, (user_id, data['name'], data['phone'], data['address'], data['email']))
    conn.commit()
    conn.close()

# --- ДАННЫЕ МАГАЗИНА ---
PRODUCTS = {
    "1": {"name": "Худи 'Оверсайз'", "price": 4500, "desc": "Удобное худи из плотного хлопка.", "img": "https://unsplash.com"},
    "2": {"name": "Футболка 'Базовая'", "price": 1900, "desc": "100% хлопок, идеальная посадка.", "img": "https://unsplash.com"},
}

# --- СОСТОЯНИЯ (FSM) ---
class AuthStates(StatesGroup):
    waiting_for_name = State()
    waiting_for_phone = State()
    waiting_for_address = State()
    waiting_for_email = State()

class SupportStates(StatesGroup):
    waiting_for_message = State()

# --- КЛАВИАТУРЫ ---
def get_main_menu(user_id):
    user = get_user(user_id)
    auth_status = "✅ Профиль заполнен" if user else "🔐 Пройти авторизацию"
    
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="👕 Каталог товаров")],
            [KeyboardButton(text=auth_status)],
            [KeyboardButton(text="🆘 Написать в поддержку")]
        ],
        resize_keyboard=True
    )
    return keyboard

def get_catalog_keyboard():
    buttons = [
        [InlineKeyboardButton(text=f"{info['name']} — {info['price']} руб.", callback_data=f"prod_{prod_id}")]
        for prod_id, info in PRODUCTS.items()
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def get_order_keyboard(prod_id):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💳 Заказать и оплатить", callback_data=f"buy_{prod_id}")],
        [InlineKeyboardButton(text="🔙 Назад в каталог", callback_data="back_to_catalog")]
    ])

# --- ОБРАБОТЧИКИ ---

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "👋 Добро пожаловать в магазин одежды!\n\n"
        "Перед покупкой рекомендуем заполнить профиль (кнопка авторизации), "
        "чтобы мы знали, куда доставить ваш заказ.",
        reply_markup=get_main_menu(message.from_user.id)
    )

# ПРОЦЕСС АВТОРИЗАЦИИ (СБОР ДАННЫХ)
@dp.message(F.text.in_({"🔐 Пройти авторизацию", "✅ Профиль заполнен"}))
async def start_auth(message: types.Message, state: FSMContext):
    user = get_user(message.from_user.id)
    if user:
        await message.answer(
            f"📋 **Ваш профиль:**\n"
            f"👤 Имя: {user['name']}\n"
            f"📞 Телефон: {user['phone']}\n"
            f"📍 Адрес: {user['address']}\n"
            f"✉️ Email: {user['email']}\n\n"
            f"Хотите изменить данные? Напишите ваше новое ФИО. Для отмены нажмите /cancel"
        )
    else:
        await message.answer(" Начнем авторизацию. Введите ваше имя и фамилию:")
    await state.set_state(AuthStates.waiting_for_name)

@dp.message(AuthStates.waiting_for_name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    # Кнопка для отправки номера телефона в один клик
    phone_keyboard = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="📱 Отправить номер", request_contact=True)]],
        resize_keyboard=True, one_time_keyboard=True
    )
    await message.answer("Введите ваш номер телефона или нажмите кнопку ниже:", reply_markup=phone_keyboard)
    await state.set_state(AuthStates.waiting_for_phone)

@dp.message(AuthStates.waiting_for_phone)
async def process_phone(message: types.Message, state: FSMContext):
    phone = message.contact.phone_number if message.contact else message.text
    await state.update_data(phone=phone)
    await message.answer("Укажите адрес доставки (Город, улица, дом, квартира):", reply_markup=types.ReplyKeyboardRemove())
    await state.set_state(AuthStates.waiting_for_address)

@dp.message(AuthStates.waiting_for_address)
async def process_address(message: types.Message, state: FSMContext):
    await state.update_data(address=message.text)
    await message.answer("Введите ваш email для отправки чека:")
    await state.set_state(AuthStates.waiting_for_email)

@dp.message(AuthStates.waiting_for_email)
async def process_email(message: types.Message, state: FSMContext):
    await state.update_data(email=message.text)
    user_data = await state.get_data()
    
    save_user(message.from_user.id, user_data)
    await state.clear()
    
    await message.answer("🎉 Данные успешно сохранены!", reply_markup=get_main_menu(message.from_user.id))

# КАТАЛОГ И ОПЛАТА
@dp.message(F.text == "👕 Каталог товаров")
async def show_catalog(message: types.Message):
    await message.answer("Выберите товар:", reply_markup=get_catalog_keyboard())

@dp.callback_query(F.data.startswith('prod_'))
async def show_product(callback_query: types.CallbackQuery):
    prod_id = callback_query.data.split('_')[1]
    product = PRODUCTS.get(prod_id)
    if product:
        caption = f"🛍 *{product['name']}*\n\n📝 {product['desc']}\n\n💰 Цена: {product['price']} руб."
        await bot.send_photo(
            callback_query.from_user.id, photo=product['img'], 
            caption=caption, parse_mode="Markdown", reply_markup=get_order_keyboard(prod_id)
        )
    await callback_query.answer()

@dp.callback_query(F.data.startswith('buy_'))
async def process_buy(callback_query: types.CallbackQuery):
    user = get_user(callback_query.from_user.id)
    if not user:
        await bot.send_message(callback_query.from_user.id, "❌ Сначала пройдите авторизацию в главном меню!")
        await callback_query.answer()
        return

    prod_id = callback_query.data.split('_')[1]
    product = PRODUCTS.get(prod_id)
    
    prices = [LabeledPrice(label=product['name'], amount=product['price'] * 100)]
    await bot.send_invoice(
        chat_id=callback_query.from_user.id,
        title=product['name'],
        description=f"Доставка на имя: {user['name']}, Адрес: {user['address']}",
        provider_token=PROVIDER_TOKEN,
        currency="rub",
        prices=prices,
        payload=f"prod_{prod_id}",
        start_parameter="fashion_shop"
    )
    await callback_query.answer()

@dp.pre_checkout_query()
async def checkout_confirm(pre_checkout_query: PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)

@dp.message(F.successful_payment)
async def success_pay(message: types.Message):
    user = get_user(message.from_user.id)
    await message.answer("🎉 Оплата прошла успешно! Мы уже собираем ваш заказ.")
    
    # Отправляем уведомление администратору / менеджеру поддержки
    if SUPPORT_ADMIN_ID:
        await bot.send_message(
            SUPPORT_ADMIN_ID,
            f"🔔 **Новый заказ!**\n"
            f"👤 Клиент: {user['name']} (@{message.from_user.username})\n"
            f"📞 Телефон: {user['phone']}\n"
            f"📍 Адрес: {user['address']}\n"
            f"💵 Сумма: {message.successful_payment.total_amount // 100} руб."
        )

# СВЯЗЬ С ПОДДЕРЖКОЙ
@dp.message(F.text == "🆘 Написать в поддержку")
async def support_start(message: types.Message, state: FSMContext):
    await message.answer(" Опишите вашу проблему или задайте вопрос одним сообщением. Отправим его администратору.")
    await state.set_state(SupportStates.waiting_for_message)

@dp.message(SupportStates.waiting_for_message)
async def support_forward(message: types.Message, state: FSMContext):
    await bot.send_message(
        SUPPORT_ADMIN_ID, 
        f"📩 **Новое обращение в поддержку!**\n"
        f"От: {message.from_user.full_name} (@{message.from_user.username} / ID: `{message.from_user.id}`)\n\n"
        f"💬 Текст: {message.text}"
    )
    await state.clear()
    await message.answer("✅ Ваше сообщение отправлено в поддержку. Менеджер свяжется с вами.", reply_markup=get_main_menu(message.from_user.id))

# Сброс любого состояния
@dp.message(Command("cancel"))
async def cancel_handler(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer("Действие отменено.", reply_markup=get_main_menu(message.from_user.id))

if __name__ == '__main__':
    init_db()
    dp.run_polling(bot)
