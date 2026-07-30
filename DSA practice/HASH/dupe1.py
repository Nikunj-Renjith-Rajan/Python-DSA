# Given an integer array nums and an integer k, return true if there are two distinct 
# indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
def containsNearbyDuplicate(nums, k):
    dic = {}
    for i in range(len(nums)):
        if nums[i] in dic and i - dic[nums[i]] <= k:
            return True
        dic[nums[i]] = i
    return False

nums = [1,2,3,1]
k = 3
print(containsNearbyDuplicate(nums,k))