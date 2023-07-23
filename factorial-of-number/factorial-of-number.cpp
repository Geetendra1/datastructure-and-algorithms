#include <iostream>

int fact(int n){
    int res = 1;
    for(int i=2; i<=n; i++){
        res = res*i;
    }
    return res;
}


int main() {
    int number = 5;
    std::cout<<fact(number);
}