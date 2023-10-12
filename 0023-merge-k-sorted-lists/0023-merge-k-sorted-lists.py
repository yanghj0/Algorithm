# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        values = []
        for i in lists:
            while i:
                values.append(i.val)
                i = i.next
        values.sort()
        cur = dummy = ListNode(0)
        for v in values:
            cur.next = ListNode(v)
            cur = cur.next
        return dummy.next