# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        data = dict()

        length = 0
        while head:
            data[length] = head
            length += 1
            head = head.next

        target = length - n
        del data[target]
        keys = list(data.keys())
        for i in range(len(keys)):
            if i + 1 >= len(keys):
                temp2 = None
            else:
                idx2 = keys[i + 1]
                temp2 = data[idx2]

            idx1 = keys[i]
            temp1 = data[idx1]
            if i + 1 >= len(keys):
                temp2 = None
            temp1.next = temp2

        if not keys:
            return None
        return data[keys[0]]
#
# node2 = ListNode(2, None)
# node1 = ListNode(1, node2)
# s = Solution()
# print(s.removeNthFromEnd(node1, 1))
