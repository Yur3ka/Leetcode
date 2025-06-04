# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        if not head.next.next:
            return head.val + head.next.val
        def reverse_list(head):
            prev = None
            current = head
            while current:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            head = prev
            return head
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        second = reverse_list(slow)
        ans = 0
        # res = []
        slow = head
        while second:
            ans = max(ans,slow.val + second.val)
            # res.append(ans)
            slow = slow.next
            second = second.next
        # print(res)
        return ans
            