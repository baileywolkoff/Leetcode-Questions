'''
Given an array of nums, and a target
Return indices of the two numbers that add up to target
Assume exactly ONE Solution
May not use same element twice
Can Return Answer in any order

date: 03-26-22
'''


'''This Solsution does not work as intended. More viable for the two sum II problem'''

# def twoSum(nums, target):
#     # make sure proper type
#     nums = sorted(list(nums)) # must be sorted
#     target = int(target)

#     # Using left and right pointers
#     l, r = 0, len(nums) - 1

#     # left pointer cannot be greater than (opr equal to) right (else solution does not exist)
#     while l < r:
#         s = nums[l] + nums[r] # calculate the sum of the two entries

#         if s < target: # must increase the sum (left pointer has to increase)
#             l += 1
#         elif s > target: # must decrease the sum (right pointer must decrease)
#             r -= 1
#         else: # the sum is equal to target. Return those indices
#             return [l,r]
    
#     # if no answer can be found, return -1
#     return -1


# print(twoSum(nums = [3,2,4], target = 6))

from time import time
            
'''Take 2'''

nums = [2,1,5,3]
target = 8


# Try a brute Force method
def bruteTwoSum(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if nums[i]+nums[j] == target:
                return[i,j]

# Using a Hash Map
# One Pass
def TwoSum(nums, target):
    prev_map = {} # val : index
    
    for i, num in enumerate(nums):
        diff = target - num
        if diff in prev_map:
            return [prev_map[diff], i]
        prev_map[num] = i
    return


t0 = time()
print(bruteTwoSum(nums,target))
t1 = time()
print(TwoSum(nums,target))
t2 = time()

print(f"Brute Force method takes {t1-t0}")
print(f"Hash Map method takes {t2-t1}")
