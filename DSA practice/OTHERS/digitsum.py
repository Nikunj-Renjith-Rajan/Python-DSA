# Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.
def addDigits(num):
    if num==0:
        return 0
    res=num%9
    if res==0:
        return 9
    return res

print(addDigits(12345))