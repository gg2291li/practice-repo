# My solution for question 21 of Leetcode
# Merge two sorted Linked List

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1 == None: return l2
        if l2 == None: return l1

        if l1.val <= l2.val:
            result = ListNode(l1.val)
            result.next = self.mergeTwoLists(l1.next, l2)
        else:
            result = ListNode(l2.val)
            result.next = self.mergeTwoLists(l1, l2.next)

        return result