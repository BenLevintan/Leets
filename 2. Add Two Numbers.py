# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 1st sulotion: naive and does not realy uses singly-linked list
class Solution1(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        num1 = 0 
        num2 = 0
        i = 0

        while l1:
            num1 += l1.val * (10 ** i)
            l1 = l1.next
            i += 1

        i = 0

        while l2:
            num2 += l2.val * (10 ** i)
            l2 = l2.next
            i += 1

        total = num1 + num2

        if total == 0:
            return ListNode(0)

        # Build the resulting linked list
        dummy = ListNode(0)
        current = dummy

        while total > 0:
            digit = total % 10
            current.next = ListNode(digit)
            current = current.next
            total //= 10

        return dummy.next

# 2nd sulotion: no int converssion and itrtates digit by figit
class Solution2(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10

            current.next = ListNode(digit)
            current = current.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next