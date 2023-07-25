#include <iostream>

// find all the prime number less than or equal to given number

// Naive solution

// void sieve(int n) {
//     int res; 
//     for(int i=2;i<=n;i++){
//         if(n%i==0){
//             std::cout<<i<<" ";
//         }
//     }
    
// }



// optimized solution

void sieve(int n){
    if (n <= 1){
        return;
    }
    
    bool isPrime[n+1];
    std::fill(isPrime, isPrime + n + 1, true);

     
    for(int i=2; i*i<=n; i++){
        if(isPrime[i]){
            for(int j=2*i; j<=n; j=j+i){
                isPrime[j] = false;
            }
        }
    }

    for(int i=2; i<=n; i++){
        if(isPrime[i]){
            std::cout<<i<<" ";
        }
    }
}



int main() {
    int number = 10;
    sieve(number);
    return 0;
}