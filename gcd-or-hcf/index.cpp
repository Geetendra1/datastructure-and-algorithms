#include <iostream>

int gcd(int a, int b){
    if(b==0)
        return a;
    return gcd(b, a%b);    
}

int main(){
    int a = 5;
    int b = 10;
    std::cout<<gcd(a,b);
    return 0;
}