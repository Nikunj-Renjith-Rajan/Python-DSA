# Given an integer array nums, find the subarray with the largest sum, and return its sum.

#WE ARE USING KADANES ALGORITHM

def maxSubArray(nums):
        csum=maxsum=nums[0]
        for i in range(1,len(nums)):
            csum=max(nums[i],csum+nums[i])
            maxsum=max(maxsum,csum)
        return maxsum

nums=[-1,2,3,-4,5,1,2,-4,3,0]
print(maxSubArray(nums))