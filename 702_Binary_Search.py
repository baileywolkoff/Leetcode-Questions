'''
Following leetcode 702
Binary Search Problem
Find Target Value inside SORTED num Array
Return index of target if found
Return -1 if not in Array
'''

def search(nums, target):
    # Proper Data Type
    nums = list(nums)
    target = int(target)

    # Initialize Pointers
    l, r = 0, len(nums) - 1
    
    # Beging Loop (left pointer should always be less than right pointer)
    while l <= r:
        # Set the mid pointer inbetween left and right
        m = (l + r) // 2

        if nums[m] < target: # want to look at all values to the right of the mid-pointer
            l = m + 1 # set left pointer to one index right of the mid
        elif nums[m] > target: # look at all values to left of mid
            r = m - 1
        else: # mid is equal to right pointer
            return m
            
    # if while loop never returns value, target must not be in array
    return -1

nums = [1,5, 8, 10, 11, 15, 19, 25]
print(search(nums, target = 10))



