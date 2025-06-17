"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list, also in reverse order.

👉 You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 Input Format:
Two singly-linked lists l1 and l2, where each node represents a single digit in reverse order

l1 = [2, 4, 3]  # Represents 342
l2 = [5, 6, 4]  # Represents 465

 output - [7, 0, 8]       # Because 342 + 465 = 807

 """

from typing import Optional

# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Helper function: Convert list to ListNode
def list_to_linkedlist(lst):
    dummy = ListNode()
    current = dummy
    for number in lst:
        current.next = ListNode(number)
        current = current.next
    return dummy.next

# Helper function: Convert ListNode to list
def linkedlist_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# Solution class
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            total = v1 + v2 + carry
            carry = total // 10

            current.next = ListNode(total % 10)
            current = current.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next

# ==== Create instance and test it ====
sol = Solution()

# Example: 342 + 465 = 807 → [2, 4, 3] + [5, 6, 4] → Output: [7, 0, 8]
l1 = list_to_linkedlist([2, 4, 3])
l2 = list_to_linkedlist([5, 6, 4])

result_node = sol.addTwoNumbers(l1, l2)
result_list = linkedlist_to_list(result_node)

print("Result Linked List:", result_list)
from typing import Optional

# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Helper function: Convert list to ListNode
def list_to_linkedlist(lst):
    dummy = ListNode()
    current = dummy
    for number in lst:
        current.next = ListNode(number)
        current = current.next
    return dummy.next

# Helper function: Convert ListNode to list
def linkedlist_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# Solution class
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            total = v1 + v2 + carry
            carry = total // 10

            current.next = ListNode(total % 10)
            current = current.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next

# ==== Create instance and test it ====
sol = Solution()

# Example: 342 + 465 = 807 → [2, 4, 3] + [5, 6, 4] → Output: [7, 0, 8]
l1 = list_to_linkedlist([2, 4, 3])
l2 = list_to_linkedlist([5, 6, 4])

result_node = sol.addTwoNumbers(l1, l2)
result_list = linkedlist_to_list(result_node)

print("Result Linked List:", result_list)
