#include <iostream>
using namespace std;

int main(){
    int number = 0;
    cout << "введите неотрицательное целое число: ";
    cin >> number;

    int tens = (number / 10) % 10;

    cout << "Число десятков: " << tens << endl;
    return 0;
}
