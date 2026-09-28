#include <iostream>
#include "3extrafile.h"
using namespace std;

int main() {
    int number = 0;
    cout << "введите неотрицательное целое число: ";
    cin >> number;

    int tens = getTensDigit(number);
    cout << "число десятков: " << tens << endl;
    return 0;
}
