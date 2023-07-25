#include <iostream>

void allDevisior(int n) {
    int i;
    for(i=1; i*i<=n; i++){
        if(n%i==0){
            std::cout<<i<<" ";
        }
    }
    for(;i>=1;i--){
        if(n%i==0){
            std::cout<<n/i<<" ";
        }
    }
}

int main() {
    
    	int n = 15;
    	
    	allDevisior(n);
    	
    	return 0;
}