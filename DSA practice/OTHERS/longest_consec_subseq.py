# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.

def longestConsecutive(nums):
        numset=set(nums)
        maxlen=0
        for num in numset:
            if num-1 not in numset:
                count=1
                while num+1 in numset:
                    count+=1
                    num+=1
                maxlen=max(count,maxlen)
        return maxlen

nums=[0,3,7,2,5,8,4,6,0,1]
print(longestConsecutive(nums))