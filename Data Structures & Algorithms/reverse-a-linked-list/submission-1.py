# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        one, two = None, head
        while two:
            tmp = two.next
            two.next = one
            one = two
            two = tmp
        return one