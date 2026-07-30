# Write code for finding the next highest number using the same digits present in the input numbers
num = input("Read a number: ")
diglist = list(num)
flag = 0

for i in range(len(diglist) - 2, -1, -1):
    if diglist[i] < diglist[i + 1]:  
        flag = 1
        break
if flag == 0:
    print("Not possible")
    exit()
for j in range(len(diglist) - 1, i, -1):
    if diglist[j] > diglist[i]:
        diglist[i], diglist[j] = diglist[j], diglist[i]
        break

res = diglist[:i + 1] + diglist[i + 1:][::-1]

next_highest = "".join(res)
print("Next highest number:", next_highest)