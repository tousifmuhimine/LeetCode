# ------------------------------------------------------------
# Problem: Add Two Numbers
# Link: https://leetcode.com/problems/add-two-numbers/
#
# Summary:
# Given two non-empty linked lists representing two non-negative integers
# in reverse order, add the two numbers and return the sum as a linked list.
# Each node contains a single digit, and the digits are stored in reverse order.
#
# Approach:
# - Use a dummy node to simplify list construction.
# - Traverse both linked lists simultaneously.
# - At each step, add corresponding digits plus any carry from previous step.
# - Create a new node with the digit (total % 10) and update carry (total // 10).
# - Continue until both lists and carry are exhausted.
# ------------------------------------------------------------

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next
