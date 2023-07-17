from typing import Optional, List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        data = []

        temp = head
        while temp:
            data.append(temp.val)
            temp = temp.next

        for i in range(0, len(data), k):
            if i + k > len(data):
                break
            temp = data[i:i + k][::-1]

            for j in range(i, i + k):
                data[j] = temp[j - i]

        temp, idx = head, 0
        while temp:
            temp.val = data[idx]
            temp, idx = temp.next, idx + 1
        return head

node7 = ListNode(4, None)
node6 = ListNode(3, node7)
node5 = ListNode(2, node6)
node4 = ListNode(1, node5)
s = Solution()
ret = s.reverseKGroup(node4, 3)
while ret:
    print(ret.val, end=" ")
    ret = ret.next