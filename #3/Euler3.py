import sys
import time

# 0 and 1 are not prime
# Sieve of Eratosthenes algorithm 

def prime_factors(n: int) -> int:
    ans = 0 #Space: O(1)
    #Space: O(sqrt(n))
    #Time: O(sqrt(n))
    isPrime = [True]*(int(n**0.5) + 1) #only need to go up to (n**0.5) because largest factor sqrt(n)

    isPrime[0] = isPrime[1] = False #These are prime values

    for num in range (2, int(n**0.5) + 1): #Time: ~O(sqrt(n))
        if isPrime[num]:
            if n % num == 0:
                ans = num
            for i in range(num*num, int(n**0.5) + 1, num): #Time: ~O(sqrt(n)/num)
                """
                num * num + num * ( num + 1 ) + num * ( num + 2 )... + num(n**0.5+num) 
                Time: ~O(sqrt(n)/num) but because of if statement occurs at every prime #
                """
                isPrime[i] = False
    """
    Total Space: O(sqrt(n)) + O(1) = O(sqrt(n))
    Total Time:  O(sqrt(n)) + O(sqrt(n)) * O(sqrt(n)/num){but occurs at every prime #} 
               = O(sqrt(n)) + O(sqrt(n)log(log(n)))
               = O(sqrt(n)log(log(n))) 
    """
    return ans

def main():
    n = 600851475143
    start_time = time.time()
    largest_prime_factor = prime_factors(n)
    end_time = end_time = time.time()
    print(
        f"The largest prime factor of  {n} is: {largest_prime_factor}")
    print(f"Time taken: {end_time - start_time:.4f} seconds")
    print("Time complexity of the problem:")


if __name__ == "__main__":
    main()
