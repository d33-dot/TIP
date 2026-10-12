#include <iostream>
using namespace std;
// while

// int main()
// {
//     double x, y;
//     cin >> x >> y;

//     int day = 1;
//     while (x < y)
//     {
//         x *= 1.1;
//         day++;
//     }

//     cout << day << endl;
//     return 0;
// }

// do while

// int main() {
//     double x, y;
//     cin >> x >> y;

//     int day = 1;
//     do {
//         x *= 1.1;
//         day++;
//     } while (x < y);

//     cout << day << endl;
//     return 0;
// }

// for

int main() {
    double x, y;
    cin >> x >> y;

    int day = 1;
    for (; x < y; day++) {
        x *= 1.1;
    }

    cout << day << endl;
    return 0;
}
