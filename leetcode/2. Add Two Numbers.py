class Solution:
    def addTwoNumbers(self, l1, l2):
        carry = 0
        head = None
        temp_head = None

        while carry or l1 is not None or l2 is not None:
            val_l1, val_l2 = 0, 0

            if l1 is not None:
                val_l1 = l1.val
                l1 = l1.next
            if l2 is not None:
                val_l2 = l2.val
                l2 = l2.next

            temp = val_l1 + val_l2 + carry
            ret = ListNode()
            ret.val = temp % 10
            carry = temp // 10
            if head is None:
                head = ret
                temp_head = ret
            else:
                temp_head.next = ret
                temp_head = temp_head.next
        return head

# s = Solution()
# print(s.addTwoNumbers([0], [0]))
# print(s.addTwoNumbers([2,4,3], [5,6,4]))
# print(s.addTwoNumbers([9,9,9,9,9,9,9], [9,9,9,9]))