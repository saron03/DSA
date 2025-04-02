# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        aheadPtr = head
        while n > 0:
            aheadPtr = aheadPtr.next
            n -= 1

    # Phase II: Move both aheadPtr and behindPtr
        behindPtr = head
        previous = None
        while aheadPtr:
            previous = behindPtr
            behindPtr = behindPtr.next 
            aheadPtr = aheadPtr.next
        if previous is None:
            return head.next
            
        previous.next = behindPtr.next
        return head


