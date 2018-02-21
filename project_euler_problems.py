import datetime

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
    reversed_digits = digits[::-1]
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
    factor = 1
    while factor <= n:
        if is_prime(factor) and n % factor == 0:
            while True:
                yield factor
                n /= factor
                if not n % factor == 0:
                    break
        factor += 1


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
        for p in get_prime_factors_list(i):
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

def sum_of_squares(first_n):
    sum = 0
    for i in range(1, first_n+1):
        sum += i * i
    return sum
    #returns the sum of the first n square numbers

def square_of_sum(first_n):
    sum = 0
    for i in range(1, first_n+1):
        sum += i
    return sum * sum
    #finds the sum of the first n numbers and returns the square of this total

def square_of_sum_minus_sum_of_squares(first_n):
    ans = square_of_sum(first_n) - sum_of_squares(first_n)
    print("The difference between the sum of the squares and square of the sum of the first " + str(first_n) +
          " natural numbers is " + str(ans))
    # problem 6 - difference between the sum of squares and square of sum of first n natural numbers

def square_of_sum_minus_sum_of_squares_efficient(n):
    ans = (3*n**3 + 2*n**2 - 3*n - 2)*n/12
    print("The difference between the sum of the squares and square of the sum of the first " + str(n) +
          " natural numbers is " + str(ans))
    # problem 6 - difference between the sum of squares and square of sum of first n natural numbers
    # Use simplified formula - approximately 5 times faster than the brute force method

# print(sum_even_fib_numbers(4000000))
# sum_of_multiples(3, 5, 1000)
# largest_prime_factor(600851475143)
# palindrome_product(4)
# lcm_of_first(20)

# start_time = datetime.datetime.now()
# square_of_sum_minus_sum_of_squares(100)
# end_time = datetime.datetime.now()
# print("Time taken: " + str(end_time - start_time))

# start_time = datetime.datetime.now()
# square_of_sum_minus_sum_of_squares_efficient(100)
# end_time = datetime.datetime.now()
# print("Time taken: " + str(end_time - start_time))

# msg = "Hello world!"
# file = open("/Users/rupes.h.vekaria/project_euler_problems/test_file.txt", "w")
# amount_written = file.write(msg)
# print(amount_written)
# file.close()
# file = open("/Users/rupesh.vekaria/project_euler_problems/test_file.txt", "r")
# print(file.read())
# file.close()