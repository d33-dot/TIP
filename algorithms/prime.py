def sieve_of_er(limit):
    if limit < 2:
        pass
    is_prime = [True]*(limit+1)
    is_prime[0] = False
    is_prime[1] = False
    while p*p <= limit:
        if is_prime[p]:
            for m in range(p*p,limit+1,p):
                is_prime[m]=False
        p+=1
    primes = [n for n, prime_flag in enumerate(is_prime) if prime_flag]
    return primes 