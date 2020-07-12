# My solution for Leetcode question 19, removing Nth Node from end of list
# I used 2 pointers to track the Nth node that needed to be removed

class Solution:
    def removeNthFromEnd(self, head, n):
        destination = head
        nAhead = destination

        for i in range(n):
            nAhead = nAhead.next
        
        if nAhead == None:
            return destination.next

        while nAhead != None:
            if nAhead.next == None:
                destination.next = destination.next.next
                break
            nAhead = nAhead.next
            destination = destination.next

        return head
        