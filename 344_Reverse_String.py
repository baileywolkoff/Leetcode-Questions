'''
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory

Date: 04-01-22
@author: Bailey Wolkoff
'''

s = ['h','e','l','l','o']


def reverseString(s):
    # Do Not return anything, modify s in-place instead

    l, r = 0, len(s)-1 # Initialize left and right pointer
    while l < r:
        # will execute below simultaneously
        s[l], s[r] = s[r], s[l] # don't need a temp variable in python
        l+=1 # increment
        r-=1 # decrement


def reverseStringStack(s):
    # Try again but using more memory
    # utlizing another array, or a 'stack'
    stack = []

    # loop through each charcter in the string
    for char in s:
        stack.append(char)
    # iterate through stack, popping the top value to string array    
    for i in range(len(stack)):
        s[i] = stack.pop()


#Final Solution using recursion
# similar to first solution, but uses more memory due to recursion.
def reverseStringRecursion(s, l=0, r=len(s)-1):
    if l<r:
        s[l], s[r] = s[r], s[l]
        reverseStringRecursion(s, l+1, r-1)

reverseStringRecursion(s)
print(s)