from typing import Optional, List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        data = []

        temp = head
        while temp:
            data.append(temp.val)
            temp = temp.next

        for i in range(1, len(data), 2):
            data[i - 1], data[i] = data[i], data[i - 1]

        temp, idx = head, 0
        while temp:
            temp.val = data[idx]
            temp, idx = temp.next, idx + 1
        return head

node7 = ListNode(6, None)
node6 = ListNode(4, node7)
node5 = ListNode(3, node6)
node4 = ListNode(1, node5)
s = Solution()
ret = s.swapPairs(node4)
while ret:
    print(ret.val, end=" ")
    ret = ret.next