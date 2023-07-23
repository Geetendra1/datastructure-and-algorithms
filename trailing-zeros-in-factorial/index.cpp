#include <iostream>

int tz(int n) {
    int res = 0;
/* The code snippet is calculating the number of trailing zeros in the factorial of a given number `n`. */
    for(int i=5; i<=n; i=i*5){
     /* The line `res = res + n/i;` is calculating the number of trailing zeros in the factorial of the
     given number `n`. It is adding the number of times `i` (which is initially 5) divides `n` to
     the current value of `res`. This is done in a loop for all values of `i` from 5 to `n`,
     incrementing `i` by multiplying it by 5 in each iteration. */
        res = res + n/i;
    }
    return res;
}


int main() {
    int number = 100;
    std::cout<< tz(number);
}