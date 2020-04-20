#  ------------------
# | key_setup module |
#  ------------------
# Input: none
# Output: public_key.txt, private_key.txt
import random


# fermat's primality test. Function is used to check if randomly generated numbers are prime
def fermat_test(prime):
    # base case
    if prime == 2 or prime == 3:
        return True
    if prime < 2 or prime % 2 == 0:
        return False
    else:
        # choose a random number between 2 and the prime minus two
        x = random.randrange(2, prime - 2)
        # initialize the boolean variable used to track tests
        indicator = True
        # repeat test 10 times
        for i in range(0, 10):
            # Fermat primality test
            if pow(x, prime - 1, prime) != 1:
                indicator = False
        return indicator


# finds a prime number in a given range of numbers
def find_prime_in_range(x, y):
    # generate a prime candidate
    candidate = random.randrange(x, y, 2)
    # keep checking odd numbers until candidate is prime
    while not fermat_test(candidate):
        candidate = random.randrange(x + 1, y, 2)
    return candidate


# my implementation of the extended euclidean algorithm
def extended_euclid(a, b):
    # q_j is the quotient, x_j, y_j are bezout coefficients
    q_j, x_j_prev, y_j = 0, 0, 0
    y_j_prev, x_j = 1, 1
    # r_j is the remainder
    r_j_prev = max(a, b)
    r_j = min(a, b)
    # loop until the remainder is 0
    while r_j != 0:
        # get quotient for each iteration
        q_j = (r_j_prev - (r_j_prev % r_j)) / r_j
        # perform euclid's extended algorithm
        temp = r_j
        r_j = r_j_prev % r_j
        r_j_prev = temp
        temp_x = x_j
        temp_y = y_j
        y_j = y_j_prev - q_j*y_j
        x_j = x_j_prev - q_j*x_j
        x_j_prev = temp_x
        y_j_prev = temp_y
    # return gcd and a^-1 (mod b) and the modular multiplicative inverse
    return r_j_prev, x_j_prev + max(a, b)


# function that generates two random prime numbers of at least 100 digits
def keygen():
    # e is given as 65537, h is the product (p-1)(q-1), inv is our private key
    e, inv, h = 65537, 0, 1
    # just in case we choose invalid keys (which is unlikely) it will keep trying
    while (e*inv) % h != 1:
        # find first prime number then find the other in range of a number 10^95 or greater
        p = find_prime_in_range(10**100, 10**150)
        # find second random prime whose difference with p is at least 10^95
        # minus 1 to correct the plus 1 in find_prime_in_range
        q = find_prime_in_range(p + 10**95 - 1, p + 10**95 + 10**150)
        n = p*q
        h = (p-1)*(q-1)
        inv = extended_euclid(e, h)[1]
    # once we have valid keys, save them
    with open('public_key.txt', 'w') as f:
        print >> f, n, '\n', e
    with open('private_key.txt', 'w') as g:
        print >> g, inv
