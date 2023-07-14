# Definition for singly-linked list.
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    #     head = None
    #     for idx in range(len(lists)):
    #         if lists[idx]:
    #             head = lists[idx]
    #             break
    #
    #     if head is None:
    #         return head
    #
    #     for now in lists[idx + 1:]:
    #         prev = head
    #         while prev and now:
    #             if now.val < prev.val:
    #                 # 언제나 head가 바뀜
    #                 temp_node = ListNode(now.val, None)
    #                 temp_node.next = prev
    #                 head = temp_node
    #                 now = now.next
    #                 prev = temp_node
    #                 continue
    #
    #             if not prev.next:
    #                 break
    #
    #             if prev.val <= now.val <= prev.next.val:
    #                 temp_node = ListNode(now.val, None)
    #                 temp_next = prev.next
    #                 prev.next = temp_node
    #                 temp_node.next = temp_next
    #                 now = now.next
    #                 prev = prev.next
    #                 continue
    #             prev = prev.next
    #
    #         if not prev.next:
    #             prev.next = now
    #     return head
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # 정렬
        head = None

        temp = []
        for now in lists:
            while now:
                temp.append(now.val)
                now = now.next
        temp.sort()

        if len(temp) == 0:
            return head

        head = ListNode(temp[0], None)
        now = head
        for i in range(1, len(temp)):
            temp_node = ListNode(temp[i], None)
            now.next = temp_node
            now = temp_node
        return head


# node2 = ListNode(5, None)
# node1 = ListNode(4, node2)
# node0 = ListNode(1, node1)
#
# node5 = ListNode(4, None)
# node4 = ListNode(3, node5)
# node3 = ListNode(1, node4)
#
# node8 = ListNode(6, None)
# node7 = ListNode(2, node8)

node27 = ListNode(7, None)
node26 = ListNode(4, node27)
node25 = ListNode(0, node26)
node24 = ListNode(-4, node25)

node17 = ListNode(7, None)
node16 = ListNode(5, node17)
node15 = ListNode(2, node16)
node14 = ListNode(1, node15)

node7 = ListNode(6, None)
node6 = ListNode(4, node7)
node5 = ListNode(3, node6)
node4 = ListNode(1, node5)
s = Solution()
ret = s.mergeKLists([node4, node14, node24])
while ret:
    print(ret.val, end=" ")
    ret = ret.next
