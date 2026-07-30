#SORT THE COLORS  (OR)  THE DUTCH NATIONAL FLAG PROBLEM 
#  You are given an array consisting of only three distinct elements (for example, an array filled randomly
# with 0s, 1s, and 2s). Your task is to sort the array in-place so that elements of the same value are adjacent, 
# and the overall values are in ascending order (all 0s, then all 1s, then all 2s).
def sortColors(nums):
    low=0
    mid=0
    high=len(nums)-1
    while(mid<=high):
        if nums[mid]==0:
            nums[low],nums[mid]=nums[mid],nums[low]
            low+=1
            mid+=1
        elif nums[mid]==1:
            mid+=1
        else:
            nums[mid],nums[high]=nums[high],nums[mid]
            high-=1
    return nums

nums=[2,0,2,1,1,0]
print(sortColors(nums))