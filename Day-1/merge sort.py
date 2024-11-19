'''10) Given an array of integers nums, sort the array in ascending order and return it. You must solve the problem without using any built-in functions in
O(nlog(n)) time complexity and with the smallest space complexity possible.'''
def Merge_sort(nums):
    for i in range(0,len(nums)-1):
        for j in range(1,len(nums)-i):
            if nums[j]<nums[j-1]:
                nums[j],nums[j-1]=nums[j-1],nums[j]
    return nums
nums=[10,30,20,15]
print(Merge_sort(nums))

Output:[10, 15, 20, 30]
