# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].

def searchRange(nums, target):
    l=0
    ind=-1
    r=(len(nums)-1)
    while l<=r:                                     #first index
        mid=(l+r)//2
        if nums[mid]==target:
            ind=mid
            r=mid-1
        elif nums[mid]>target:
            r=mid-1
        else:
            l=mid+1
    l=0
    ind2=-1
    r=(len(nums)-1)
    while l<=r:                                     #last index
        mid=(l+r)//2
        if nums[mid]==target:
            ind2=mid
            l=mid+1
        elif nums[mid]>target:
            r=mid-1
        else:
            l=mid+1
    return([ind,ind2])

nums = [5,7,7,8,8,10]
target = 8
print(searchRange(nums,target))