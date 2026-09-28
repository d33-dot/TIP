#include <iostream>
#include <cmath>
using namespace std;

int main(){
    double a = 0.0;
    double b = 0.0;

    cout << "введите катеты a и b: ";
    cin >> a >> b;

    double c = sqrt(a * a + b * b);

    cout << "Гипотенуза: " << c << endl;
    return 0;
}
