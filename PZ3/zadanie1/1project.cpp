#include <iostream>
#include "extrafile.h"
using namespace std;

int main(){
    double a = 0.0;
    double b = 0.0;

    cout << "Введите катеты a и b: ";
    cin >> a >> b;

    double c = Hypotenuse(a, b);

    cout << "Гипотенуза: " << c << endl;
    return 0;
}
