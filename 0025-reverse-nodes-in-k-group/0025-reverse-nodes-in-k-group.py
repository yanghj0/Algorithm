# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cnt = 0
        temp = head
        # 1. 링크드리스트 개수 세기
        while temp:
            temp = temp.next
            cnt += 1
        
        n = cnt//k # 2. 뒤집어야하는 횟수 계산
        prev = dummy = ListNode(0) # 3. prev 정의
        dummy.next = head

        while n:  # 4. cur, next 정의
            cur = prev.next
            nex = cur.next
            for i in range(1,k):
                cur.next = nex.next
                nex.next = prev.next
                prev.next = nex
                nex = cur.next
            prev = cur
            n -= 1
        return dummy.next