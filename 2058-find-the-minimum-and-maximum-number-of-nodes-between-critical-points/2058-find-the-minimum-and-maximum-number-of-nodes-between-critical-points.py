# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        nums = []
        start = None
        last = None
        prev = None
        cur = head
        i = 0
        min_dis = float('inf')
        max_dis = -1
        while cur and cur.next:
            if prev and (prev > cur.val < cur.next.val or prev < cur.val > cur.next.val):
                start = i if start == None else start
                if last:
                    max_dis = i - start
                    min_dis = min(i - last, min_dis)
                last = i
            prev = cur.val
            cur = cur.next
            i += 1
        min_dis = -1 if min_dis == float('inf') else min_dis
        return [min_dis, max_dis]