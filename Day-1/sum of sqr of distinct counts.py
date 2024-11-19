'''You are given a 0-indexed integer array nums. The distinct count of a subarray of nums is defined as: Let nums[i..j] be a subarray of nums consisting of all the 
indices from i to j such that 0 <= i <= j < nums.length. Then the number of distinct values in nums[i..j] is called the distinct count of nums[i..j]. Return the sum 
of the squares of distinct counts of all subarrays of nums. A subarray is a contiguous non-empty sequence of elements within an array.'''
def subarray(nums):
    sum=0
    n=len(nums)
    for i in range(0,n):
        ans=[]
        for j in range(i,n):
            if nums[j] not in ans:
                ans.append(nums[j])
            sum+=len(ans)**2
    return sum
num=[1,2,1]
print(subarray(num)) 

# Output: 15

'''Explanation:
For nums = [1, 2, 1]:

Subarray [1] has distinct count 1 → 1^2 = 1
Subarray [1, 2] has distinct count 2 → 2^2 = 4
Subarray [1, 2, 1] has distinct count 2 → 2^2 = 4
Subarray [2] has distinct count 1 → 1^2 = 1
Subarray [2, 1] has distinct count 2 → 2^2 = 4
Subarray [1] has distinct count 1 → 1^2 = 1
Sum of squares = 1 + 4 + 4 + 1 + 4 + 1 = 15.'''
