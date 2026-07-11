#Find all unique triplets in an array nums which gives the sum zero
def threesum(nums):
    nums.sort()
    res=[]
    for i in range(len(nums)):
        if i>0 and nums[i]==nums[i-1]:
            continue
        l=i+1                                       #Twosum logic
        r=len(nums)-1
        while(l<r):
            s=nums[i]+nums[l]+nums[r]
            if s>0:
                r-=1
            elif s<0:
                l+=1
            else:
                res.append([nums[i],nums[l],nums[r]])
                l+=1
                while l<r and nums[l]==nums[l-1]:           #to avoid duplicate values
                    l+=1
    return res

arr=[-1,1,0,2,3,1,-3]                               #RESULT:[[-3, 0, 3], [-3, 1, 2], [-1, 0, 1]]
print(threesum(arr))
                
