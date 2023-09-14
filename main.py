# Python Program to find first n prime numbers
from math import sqrt


def generate_first_odd_composite_numbers(n):
    odd_composite_numbers = []
    i = 9
    while len(odd_composite_numbers) <= n:
        if not isPrime(i) and (i % 2 != 0):
            odd_composite_numbers.append(i)
        i = i + 1
    return odd_composite_numbers


def generate_primes_until(n):
    primes = []
    for i in range(1, n):
        if isPrime(i):
            primes.append(i)

    return primes


def isPrime(num):
    # If given number is greater than 1
    if num > 1:
        # Iterate from 2 to n / 2
        for i in range(2, int(num / 2) + 1):
            # If num is divisible by any number between
            # 2 and n / 2, it is not prime
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False


def goldbachs_conjecture_checker(num, primes):
    x = num
    generated_primes_until = primes
    last_y = -1
    last_z = -1
    could_be_written = False
    for y in generated_primes_until:
        if x <= y:
            break
        last_y = y
        last_z = sqrt((x - y) / 2)
        if last_z.is_integer():
            could_be_written = True
            break

    if could_be_written:
        print(str(x) + " = " + str(last_y) + " + 2*" + str(last_z) + "^2")
    else:
        print(str(x) + " could not be written")


if __name__ == '__main__':
    oddCompositeNumbers = generate_first_odd_composite_numbers(10000)
    prime_numbers = generate_primes_until(oddCompositeNumbers[len(oddCompositeNumbers) - 1])
    print("x = y + 2*z^2")
    print("z = ((x-y)/2)^(1/2)")
    print("x > y; z є N")
    print("5777 is the first such number")
    print()
    for number in oddCompositeNumbers:
        goldbachs_conjecture_checker(number, prime_numbers)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
