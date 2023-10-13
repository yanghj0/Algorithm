# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# dummy: 복제된리스트(x), 새로운빈리스트(x), !!기존노드의 처음에 위치하는 가상노드!!
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy

        while cur.next and cur.next.next:
            node1, node2 = cur.next, cur.next.next
            cur.next,node1.next,node2.next = node2, node2.next,node1
            cur = node1
        return dummy.next