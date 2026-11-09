#include <iostream>
using namespace std;

int main(){
    int a;
    cin>>a;
    a = abs(a);
    int last = a%10;

    while (a>=10){
        a /= 10;
    }
    int first = a;

    cout<<first<<'\n';
    cout<<last<<'\n';
}