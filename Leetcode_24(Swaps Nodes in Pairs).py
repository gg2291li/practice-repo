# My solution for Swap Nodes in Pairs, Leetcode 24, using two pointers and recursion

# Definition for singly-linked list.

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


class Solution:
    def swapPairs(self, head):
        if head == None: return None
        if head.next == None: return head

        old_head = head
        head = head.next
        old_head.next = self.swapPairs(head.next)
        head.next = old_head

        return head