class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        sieve = [True] * (right + 1)
        sieve[0] = sieve[1] = False  
        for i in range(2, int(right ** 0.5) + 1):
            if sieve[i]: 
                for j in range(i * i, right + 1, i):
                    sieve[j] = False

       
        primes = [i for i in range(left, right + 1) if sieve[i]]
        
        if len(primes) <= 1:
            return [-1, -1]

        min_dif = float('inf')
        res = []
        for i in range(1, len(primes)):
            diff = primes[i] - primes[i - 1]
            if diff < min_dif:
                min_dif = diff
                res = [primes[i - 1], primes[i]]

        return res
