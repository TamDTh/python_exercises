import argparse


def main(args):
    N = args.nprime
    primes = []
    init_prime = 2
    while len(primes) < N:
        prime_test = [init_prime for i in primes if init_prime % i == 0]
        primes += [] if prime_test else [init_prime]
        init_prime += 1

    if args.firstindex:
        print(primes[0])
    else:
        print(primes)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process N primes')
    parser.add_argument("-n", "--nprime", dest="nprime", type=int,
                        help="An integer for N prime numbers", metavar="Num", required=True)
    parser.add_argument("-f", "--firstindex", dest="firstindex", type=bool,
                        help="Print the first index of N primes", required=False)
    args = parser.parse_args()
    main(args)


