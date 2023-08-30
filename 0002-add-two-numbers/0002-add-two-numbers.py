# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        answer = ListNode() # Linked List로 리턴
        p = answer # ListNode를 가리키는 포인터
        carry = 0

        # 처리해야 할 수가 남았을 때
        while l1 or l2 or carry:
            sum = 0 # 자릿수의 합
            if l1:
                sum += l1.val # l1의 현재 자리수 더하기
                l1 = l1.next # l1의 다음 자리수 더하기
            if l2:
                sum += l2.val
                l2 = l2.next
            sum += carry
            carry = sum//10 # 올림수가 두자리수면 나눠주기
            sum %= 10

            # 리턴할 노드
            p.next = ListNode(sum) # 현재 가리키는 노드에 새로운 노드 연결
            p = p.next

        return answer.next