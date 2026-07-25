#Find all unique combinations of k size which add up to given target
def kSum(nums,target,k):
    res=[]
    arr=[]
    nums.sort()
    print(nums)
    def recursiveKSum(k,start,target):                     #Created a helper function
        if k!=2:
            for i in range(start,len(nums)-k+1):
                if i>start and nums[i]==nums[i-1]:
                    continue
                print(nums[i],end=" ")
                arr.append(nums[i])
                print(arr)
                recursiveKSum(k-1,start+1,target-nums[i])
                arr.pop()                                   #To reinitialize the list on its way out
            return                               
        #Sorted array TwoSum logic
        l=start
        r=len(nums)-1
        while l<r:
            if nums[l]+nums[r]<target:
                l+=1
            elif nums[l]+nums[r]>target:
                r-=1
            else:
                res.append(arr+[nums[l],nums[r]])
                l+=1
                while l<r and nums[l]==nums[l-1]:
                    l+=1
    recursiveKSum(k,0,target)
    return res

arr=[1,0,-1,2,-2,0]
target=0
k=4
print(kSum(arr,target,k))
    