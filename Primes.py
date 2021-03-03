class Primes:

    # finds all primes below n
    # uses the sieve of Eratosthenes  algorithm
    @staticmethod
    def primes_below(n: int):
        primeList = []

        prime = [True for i in range(n + 1)]
        prime[0] = True
        prime[1] = False
        for i in range(2,n+1):
            if prime[i]:
                primeList.append(i)
                j = i + i
                while j <= n:
                    prime[j] = False
                    j += i
        return primeList


