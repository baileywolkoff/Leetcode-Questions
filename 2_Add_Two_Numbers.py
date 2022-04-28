'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Date: 03-30-22
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

l1 = [2,4,3]
l2 = [5,6,4]

def addTwoNumbers(l1,l2):
    dummy = ListNode()
    cur = dummy

    while l1 or l2:
        
    