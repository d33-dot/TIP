#include <iostream>
#include <cmath>
using  namespace std;

double Hypotenuse(double a, double b) {
    return sqrt(a * a + b * b);
}

int main() {
    double a = 0.0;
    double b = 0.0;

    cout << "введите катеты a и b: ";
    cin >> a >> b;

    double c = Hypotenuse(a, b);

    cout << "Гипотенуза: " << c << endl;
    return 0;
}