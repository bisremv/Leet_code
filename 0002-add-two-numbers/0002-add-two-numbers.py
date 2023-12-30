# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode()
        current = dummy_head
        carry = 0

        while l1 or l2 or carry:
        # Get the values of the current nodes (if available)
            value1 = l1.val if l1 else 0
            value2 = l2.val if l2 else 0

        # Calculate the sum and carry
            total = value1 + value2 + carry
            carry = total // 10

        # Create a new node with the remainder of the division
            current.next = ListNode(total % 10)
            current = current.next

        # Move to the next nodes (if available)
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy_head.next
            