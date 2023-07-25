#include <iostream>

void printPrimeFactors(int n){
    if (n<=1)
        return ;
    

    
    for(int i=2; i*i<=n; i++){
        while(n%i==0){
            std::cout<<i<<" ";
            n = n/i;
        }
    }
    //if the number is prime, it will be printed here as well.
    if(n>1)
        std::cout<<n<<" ";
}


int main() {
    
    	int n = 15;
    	
    	printPrimeFactors(n);
    	
    	return 0;
}