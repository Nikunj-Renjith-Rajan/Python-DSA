# You are given a positive integer n.
# Return the maximum product of any two digits in n.
# Note: You may use the same digit twice if it appears more than once in n.

#METHOD 1-BRUTE FORCE
def maxProduct1(n):
    org=n
    lst=[]
    while n>0:
        lst.append(n%10)
        n//=10
    lst.sort()
    return lst[-1]*lst[-2]

#METHOD 2-OPTIMAL
def maxProduct2(n):
    max1 = 0
    max2 = 0
    while n > 0:
      digit = n % 10
      if digit > max1:
        max2 = max1
        max1 = digit
      elif digit > max2:
        max2 = digit
      n //= 10
    return max1 * max2


n=int(input("Read a number:"))
print("Max product of 2 digits is : ",maxProduct1(n))
print("Max product of 2 digits is : ",maxProduct2(n))