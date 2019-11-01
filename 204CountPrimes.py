# 204. Count Primes
# Easy

# Count the number of prime numbers less than a non-negative number, n.

# Example:

# Input: 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
'''
 this works but it is brute force


class Solution:
    prime = []
    def countPrimes(self, n: int) -> int:
        
        for k in range(1, n):
            if self.isPrime(k):
                self.prime.append(k)
        print(self.prime)
        return len(self.prime)

    def isPrime(self, N) -> bool:
        if (N <= 1): 
            return False
        # Check from 2 to n-1 
        for i in range(2, N//2): 
            if (N % i == 0): 
                return False
        return True

res = Solution().countPrimes(200)
print(res)
'''

class Solution:
    def countPrimes(self, n: int) -> int:
        plist = [False for i in range(n+1)]
        p = 2
        while p*p < n:
            if not plist[p]:
                for i in range(p*p, n+1, p):
                    plist[i] = True
            p += 1
        count = 0
        for p in range(2,n):
            if not plist[p]:
                count += 1
        return count
res = Solution().countPrimes(5000)
print(res)


