#Find the number of 1 bits in the binary conversion of the input number
def hammingweight(n):
    res=0
    while(n!=0):
        res+=1
        n=n&(n-1)
    return res

n=int(input("Read a number:"))
print(f"There are {hammingweight(n)} number of 1(s) in {n}")