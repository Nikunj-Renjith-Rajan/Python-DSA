# The count-and-say sequence is a sequence of digit strings defined by the recursive formula:
# countAndSay(1) = "1"
# countAndSay(n) is the run-length encoding of countAndSay(n - 1).

def RLE(sequence):
    curr = sequence[0]
    count = 0
    ans = ""
    for num in sequence:
        if curr == num:
            count += 1
        else:
            ans += str(count)+curr
            curr = num
            count = 1
    return ans + str(count)+curr

def countAndSay(n):
    if n == 1:
        return "1"
    return RLE(countAndSay(n - 1))

n=int(input("Read a number:"))
print(countAndSay(n))

# Input: n = 4
# Output: "1211"
# Explanation:
# countAndSay(1) = "1"
# countAndSay(2) = RLE of "1" = "11"
# countAndSay(3) = RLE of "11" = "21"
# countAndSay(4) = RLE of "21" = "1211"