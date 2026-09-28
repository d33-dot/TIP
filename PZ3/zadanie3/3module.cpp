#include <iostream>
using namespace std;

int getTensDigit(int number) {
    return (number / 10) % 10;
}

int main() {
    int number = 0;
    cout << "введите неотрицательное целое число: ";
    cin >> number;

    int tens = getTensDigit(number);
    cout << "число десятков: " << tens << endl;
    return 0;
}
