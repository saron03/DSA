# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        while head and head.val == val:
            head = head.next
        current = head  
        previous = None  
        while current:
            if current.val == val:
                previous.next = current.next  
            else:
                previous = current  
            current = current.next  
        return head