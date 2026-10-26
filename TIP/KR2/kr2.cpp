#include <iostream>
#include <numeric>
using namespace std;

// задание 1
// long long quick_power(long long base, long long exp) {
//     long long result = 1;
//     while (exp > 0) {
//         if (exp % 2 == 1) {
//             result *= base;
//         }
//         base *= base;
//         exp /= 2;
//     }
//     return result;
// }
// int main() {
//     cout << quick_power(10, 12) << endl; 
//     return 0;
// }

//задагие 2.1
// long long gcd_recursive(long long a, long long b) {
//     if (b == 0) {
//         return a;
//     }
//     return gcd_recursive(b, a % b);
// }
// int main() {
//     long long a, b;
//     if (cin >> a >> b) {
//         cout << gcd_recursive(a, b) << endl;
//     }
//     return 0;
// }

//задание 2.2
// int main() {
//     long long a, b;
//     if (cin >> a >> b) {
//         cout << gcd(a, b) << endl;
//     }
//     return 0;
// }

// задание 3
// void move_ingredients(int n, int start, int target, int auxiliary) {
//     if (n == 1) {
//         cout << "Ingredient 1 move from " << start << " to " << target << "\n";
//         return;
//     }
    
//     move_ingredients(n - 1, start, auxiliary, target);
    
//     cout << "Ingredient " << n << " move from " << start << " to " << target << "\n";

//     move_ingredients(n - 1, auxiliary, target, start);
// }
// int main() {
//     int n;
//     if (cin >> n) {
//         move_ingredients(n, 1, 3, 2);
//     }
//     return 0;
// }
