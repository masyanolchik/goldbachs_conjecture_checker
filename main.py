# Python Program to find first n prime numbers
from math import sqrt


def generateFirstOddCompositeNumbers(n):
    oddCompositeNumbers = []
    i = 9
    while len(oddCompositeNumbers) <= n:
        if not isPrime(i) and (i % 2 != 0):
            oddCompositeNumbers.append(i)
        i = i + 1
    return oddCompositeNumbers


def generatePrimesUntil(n):
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


def goldbachs_conjecture_checker(num):
    x = num
    generated_primes_until = generatePrimesUntil(num)
    last_y = -1
    last_z = -1
    could_be_written = False
    for y in generated_primes_until:
        last_y = y
        last_z = sqrt((x - y) / 2)
        if last_z.is_integer():
            could_be_written = True
            break

    if could_be_written:
        print(str(x) + " = " + str(last_y) + " + 2*" + str(last_z))
    else:
        print(str(x) + " could not be written")


if __name__ == '__main__':
    oddCompositeNumbers = generateFirstOddCompositeNumbers(10000)
    print("x = y + 2*z^2")
    print("z = ((x-y)/2)^(1/2)")
    print("x > y; z є N")
    print("5777 is the first such number")
    print()
    for number in oddCompositeNumbers:
        goldbachs_conjecture_checker(number)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
