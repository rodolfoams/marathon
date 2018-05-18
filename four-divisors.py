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
    for i in xrange(n+1):
        v = i
        found = False
        for p in primes:
            if p > v: break
            if v % p == 0:
                if not found:
                    if v == p**3:
                        ctr += 1
                        values.append(i)
                        break
                    elif v % p**2 == 0:
                        break
                    else:
                        v /= p
                        found = True
                else:
                    if v == p:
                        ctr += 1
                        values.append(i)
                    break
    print ctr
    # print values

if __name__ == "__main__":
    main(argv[1:])