#include <iostream>
using namespace std;

int main(){
    int A[4] = {1,4,7,10};
    int B[4] = {2,3,8,12};
    int C[size(A)+size(B)] = {};
    fill(begin(C),end(C),1);
    int i = 0;
    int j = 0;
    int count = 0;
    while (i <= size(A) && j <= size(B)){
        if (A[i] < B[j]){
            C[count] = A[i];
            i++;
        }
        else{
            C[count] = B[j];
            j++;
        }
        count++;
    }
    for (int el : C) {
        cout<<el<<' ';
    }
}