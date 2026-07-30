#Given an array of numbers, move all zeroes to the left of the array in-place
def moveZero(nums):
    insert_pos=0
    for i in range(len(nums)):
        if nums[i]!=0:
            nums[insert_pos],nums[i]=nums[i],nums[insert_pos]
            insert_pos+=1
    return nums

nums=[1,0,3,3,4,5,0,0,2,3,0,3,4]
print(moveZero(nums))