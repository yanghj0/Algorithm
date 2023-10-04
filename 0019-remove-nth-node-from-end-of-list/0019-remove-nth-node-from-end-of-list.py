# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        slow = head

        # n번째 수를 삭제하기 위해 n으로 이동
        for i in range(n):
            fast = fast.next 

        if not fast:
            return head.next # 다음 노드를 가리킴으로서 해당 노드 삭제
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next # slow도 n번째 다음 노드를 가리키며 해당노드 삭제

        return head