def sum_of_multiples(m1, m2, max):
    multiples = []
    for i in range(max):
        if i % m1 == 0 or i % m2 == 0:
            multiples.append(i)

    total = 0
    for num in multiples:
        total += num

    print total


def fib(n):
    if n == 0:
        return 1
    elif n == 1:
        return 2
    else:
        return fib(n - 1) + fib(n - 2)


def sum_even_fib_numbers(max):
    i = 1
    total = 0
    while fib(i) < max:
        n = fib(i)
        if n % 2 == 0:
            total += n
        i += 1
    return total


def is_prime(n):
    found_factor = False
    test_factor = 2
    while not found_factor and test_factor <= (n / 2):
        if n % test_factor == 0:
            found_factor = True
        test_factor += 1

    if n == 0 or n == 1 or found_factor:
        return False
    else:
        return True


def largest_prime_factor(n):
    num = n
    if is_prime(n):
        print("The largest prime factor of " + str(n) + " is " + str(n))
    elif n == 1:
        print("1 has no factors other than itself.")
    else:
        max_prime = 0
        factor = 2
        while factor <= n / 2:
            print("Checking factor " + str(factor) + " for " + str(n))

            if n % factor == 0 and is_prime(factor):  # if factor is a prime factor of n
                if factor > max_prime:
                    max_prime = factor

                while True:
                    n /= factor
                    if not n % factor == 0:
                        break

            print("Largest prime so far is " + str(max_prime) + "\n")
            if n == 1:
                n *= factor
                break
            factor += 1

        print("The largest prime factor of " + str(num) + " is " + str(n))


def is_palindrome(n):
    digits = list(str(n))
    reversed_digits = list(str(n))
    reversed_digits.reverse()
    if digits == reversed_digits:
        return True
    else:
        return False


def palindrome_product(digits):
    limit = 10 ** digits - 1
    max_pal = 0
    num1 = 0
    num2 = 0
    i = 0
    while i <= limit:
        j = i
        while j <= limit:
            ans = i * j
            print(str(i) + " x " + str(j))
            if is_palindrome(ans) and ans > max_pal:
                max_pal = ans
                num1 = i
                num2 = j
            j += 1
        i += 1
    if max_pal == 0:
        print("There are no palindromes made from the product of two " + str(digits) + " digit numbers.")
    else:
        print("The largest palindrome made from the product of two " + str(digits) + " numbers is " + str(
            max_pal) + " = " + str(num1) + "x" + str(num2))
        # problem 4 - largest palindrome made from the product of two n-digit numbers


def get_prime_factors_list(n):
    prime_factors_list = []
    factor = 1
    while factor <= n:
        if is_prime(factor) and n % factor == 0:
            while True:
                prime_factors_list.append(factor)
                n /= factor
                if not n % factor == 0:
                    break
        factor += 1
    return prime_factors_list


def lcm_of_first(limit):
    max_prime = 0
    i = 1
    while i <= limit:
        if is_prime(i):
            max_prime = i
        i += 1
    # count the number of primes there are in the range and find the largest prime
    # then you know all prime factors found will be less than this max
    highest_prime_powers_array = [0] * (max_prime + 1)
    print(len(highest_prime_powers_array))

    i = 1
    while i <= limit:  # for each number up to max, create an ArrayList of prime factors
        occurrences = [0] * (max_prime + 1)
        prime_factors = get_prime_factors_list(i)
        for p in prime_factors:
            occurrences[p] += 1
        # get an array of the amount of each prime factor
        # e.g occurrences[5] will give the number of 5's in the prime factorisation
        j = 2
        while j <= max_prime:  # for - find the highest power of each prime factor
            if occurrences[j] > highest_prime_powers_array[j]:
                highest_prime_powers_array[j] = occurrences[j]
            j += 1
        i += 1

    LCM = 1
    k = 2
    while k <= max_prime:  # get the product of prime factors
        LCM *= k ** highest_prime_powers_array[k]
        k += 1

    print("The LCM of the numbers from 1 to " + str(limit) + " is " + str(LCM))
    # problem5 - LCM of set of numbers from 1 to max

# print(sum_even_fib_numbers(4000000))
# sum_of_multiples(3, 5, 1000)
# largest_prime_factor(600851475143)
# palindrome_product(4)
# lcm_of_first(20)
