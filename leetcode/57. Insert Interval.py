class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()

        ret = [intervals[0]]

        def interval(left, right):
            (ll, lr), (rl, rr) = left, right
            if rl <= lr:
                return True
            return False

        for i in range(1, len(intervals)):
            prev_ll, prev_lr = ret[-1]
            now_rl, now_rr = intervals[i]
            if interval(ret[-1], intervals[i]):
                ret.pop()
                ret.append([min(prev_ll, now_rl), max(prev_lr, now_rr)])
            else:
                ret.append([now_rl, now_rr])
        return ret