#include <iostream>
using namespace std;

class Analyzer {
private:
    int value;

public:
    Analyzer(int val) : value(val) {}

    int getTens() const {
        return (value / 10) % 10;
    }
};

int main() {
    int number = 0;
    cout << "введите неотрицательное целое число: ";
    cin >> number;

    Analyzer analyzer(number);

    cout << "число десятков: " << analyzer.getTens() << endl;
    return 0;
}
