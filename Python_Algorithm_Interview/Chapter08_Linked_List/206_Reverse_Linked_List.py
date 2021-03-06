# 역순 연결 리스트(219p)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, cur = None, head
        while cur:
            next, cur.next = cur.next, prev
            prev, cur = cur, next
        return prev
