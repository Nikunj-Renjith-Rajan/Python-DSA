# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

def climbStairs(n):
    if n<=2:
        return n
    prev1,prev2=1,2
    for i in range(3,n+1):
        curr=prev1+prev2
        prev1=prev2
        prev2=curr
    return prev2

print(climbStairs(5))