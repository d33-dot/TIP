#include <iostream>
#include <cmath>
using namespace std;

class Triangle {
private:
    double sideA;
    double sideB;

public:
    Triangle(double a, double b) : sideA(a), sideB(b) {}

    double getHypotenuse() const {
        return sqrt(sideA * sideA + sideB * sideB);
    }
};

int main() {
    double a = 0.0;
    double b = 0.0;

    cout << "введите катеты a и b: ";
    cin >> a >> b;

    Triangle triangle(a, b);

    cout << "гипотенуза: " << triangle.getHypotenuse() << endl;
    return 0;
}
