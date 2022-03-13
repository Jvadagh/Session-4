# first exercise .list the factors of the integers 1...max
max = 20
n = 1
while n <= max:
    factor = 1
    print(end=str(n) + ': ')
    while factor <= n:
        if n % factor == 0:
            print(factor, end=' ')
        factor += 1
    print()
    n += 1


# secend exercise .(just type code)
"""max_value = int(input('display primes up to what value? ' ))
value = 2 # smalles prime number
while value <= max:
    # see if value is prime
    is_prime = True # Provisionally, value is prime
    # try all possible factors from 2 value - 1
    trial_factor = 2
    while trial_factor < value:
        if value % trial_factor == 0:
            is_prime = False    # found a factor
            break               # no need to continue; its not prime
        trial_factor += 1       # try the next potential factor
    if is_prime:
        print(value, end= ' ')  # display the prime number
    value += 1                  # try the next potential prime number
print()                         # move cursor down to next line"""

