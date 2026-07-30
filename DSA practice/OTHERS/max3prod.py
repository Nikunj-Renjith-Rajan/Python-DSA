# Given an integer array nums, find three numbers whose product is maximum and return the maximum product.
def maximumProduct(nums):
        max1 = max2 = max3 = float('-inf')
        min1 = min2 = float('inf')
        for n in nums:
            if n > max1:
                max3 = max2
                max2 = max1
                max1 = n
            elif n > max2:
                max3 = max2
                max2 = n
            elif n > max3:
                max3 = n
            if n < min1:
                min2 = min1
                min1 = n
            elif n < min2:
                min2 = n
        option1 = max1*max2*max3
        option2 = min1*min2*max1
        return max(option1,option2)

nums=[-100,-2,-3,1]
print(maximumProduct(nums))