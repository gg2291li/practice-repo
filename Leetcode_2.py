#The 1 pass python solution for question "Add Two Numbers", using simple next pointers with carry forward digit if any

# Definition for singly-linked list.
 class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


class Solution:
        
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None: return l2
        if l2 == None: return l1

        result = ListNode()
        current = result
        current.val = (l1.val + l2.val) % 10
        if l1.val + l2.val >= 10:
            carry = 1
        else:
            carry = 0
        L1pointer = l1.next
        L2pointer = l2.next
        L1val = 0
        L2val = 0


        while (L1pointer != None or L2pointer != None or carry == 1):
            if L1pointer != None: L1val = L1pointer.val
            if L2pointer != None: L2val = L2pointer.val
            temp = ListNode((L1val + L2val + carry) % 10)
            current.next = temp
            current = current.next

            carry = 1 if (L1val + L2val + carry) >= 10 else 0
            if L1pointer != None: L1pointer = L1pointer.next
            if L2pointer != None: L2pointer = L2pointer.next
            L1val = 0
            L2val = 0



        return result