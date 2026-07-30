# Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray 
# whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
def minSubArrayLen(target, nums):
    if len(nums)==0:
        return 0
    subsum=0
    size=float('inf')
    left=0
    right=0
    for right in range(len(nums)):
        subsum+=nums[right]
        while subsum>=target:
            size=min(size,right-left+1)
            subsum-=nums[left]
            left+=1
    return 0 if size==float('inf') else size

target=7
nums=[2,3,1,2,4,3]
print(minSubArrayLen(target,nums))
