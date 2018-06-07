from sys import argv

def generate_primes(n):
    primes = list()
    is_prime = [True] * ( n + 1 )
    is_prime[0] = False
    is_prime[1] = False
    for i in xrange( len( is_prime ) ):
        if is_prime[i]:
            primes.append(i)
            for j in xrange( 2, len( is_prime ) / i ):
                is_prime[j*i] = False
    return primes

def main(args):
    n = int(args[0])
    primes = generate_primes(n)
    ctr = 0
    values = list()
    for i in xrange(len(primes)):
        p1 = primes[i]
        if p1**2 >= n:
            break
        if p1**3 <= n:
            values.append(p1**3)
            ctr += 1
        for j in xrange(i+1, len(primes)):
            p2 = primes[j]
            if p1*p2 > n:
                break
            if p1*p2 <= n:
                values.append(p1*p2)
                ctr += 1
    print ctr
    # print sorted(values)

if __name__ == "__main__":
    main(argv[1:])