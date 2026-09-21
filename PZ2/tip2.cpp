#include <iostream>
using namespace std;

int main() {
    int a = 1;
    int b = 1;
    int k;
    cin >> k;
    for (int i = 1;i<=k;i++){
        a = a*i;
        b = b*a;
    }
    cout<<b;
}