# You are given an integer n. Your task is to compute the GCD (greatest common divisor) of two values:
# sumOdd: the sum of the smallest n positive odd numbers.
# sumEven: the sum of the smallest n positive even numbers.
# Return the GCD of sumOdd and sumEven.
def gcdOfOddEvenSums(n):
    return n

n=int(input("Read a number:"))
print("Result is ",gcdOfOddEvenSums(n))


# Sum of First n Odd Numbers: n**2
# Sum of First n Even Numbers: n**2 + n
# GCD Calculation: gcd(sumOdd,sumEven) = gcd(n**2, n**2 + n) = gcd(n**2, n) = n