# -*- coding: utf-8 -*-
# Time    : 2019/12/5 17:10
# Author  : Tianxiao Gao
# Contact : gtx@pku.edu.cn
# File    : 2.py
"""
Description : Add Two Numbers
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = (l1.val + l2.val) // 10
        result = ListNode((l1.val + l2.val) % 10)
        output = result
        while l1.next or l2.next:
            if l1.next and l2.next:
                l1 = l1.next
                l2 = l2.next
                result.next = ListNode((l1.val + l2.val + carry) % 10)
                carry = (l1.val + l2.val + carry) // 10
            elif l1.next and not l2.next:
                l1 = l1.next
                result.next = ListNode((l1.val + carry) % 10)
                carry = (l1.val + carry) // 10
            else:
                l2 = l2.next
                result.next = ListNode((l2.val + carry) % 10)
                carry = (l2.val + carry) // 10
            result = result.next
        if carry == 1:
            result.next = ListNode(1)

        return output


num1 = ListNode(0)
# num1.next = ListNode(4)
# num1.next.next = ListNode(3)
num2 = ListNode(7)
num2.next = ListNode(3)
# num2.next.next = ListNode(4)
sol = Solution()
res = sol.addTwoNumbers(num1, num2)
print(res.val)
print(res.next.val)
