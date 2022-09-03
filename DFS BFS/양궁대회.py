import sys
sys.setrecursionlimit(100000)

def solution(n, info):
    ans = []

    pivot = 0
    for idx, item in enumerate(info):
        if item != 0:
            pivot += (10 - idx)

    def dfs(idx, score, rival, remain, arrows):
        if idx == 10 or remain == 0:
            arrows[idx] += remain
            arrows.reverse()
            if score > rival:
                ans.append((score - rival, arrows))
            return

        temp = [i for i in arrows]
        if info[idx] < remain:
            temp[idx] += info[idx] + 1
            temp_score = score + (10 - idx)
            temp_rival = rival - (10 - idx if info[idx] > 0 else 0)
            temp_remain = remain - (info[idx] + 1)
            dfs(idx + 1, temp_score, temp_rival, temp_remain, temp)

        dfs(idx + 1, score, rival, remain, arrows)

    dfs(0, 0, pivot, n, [0] * 11)
    ans.sort(reverse=True)
    if len(ans) < 1:
        return [-1]

    ans = ans[0][1]
    ans.reverse()

    return ans

print(solution(5,	[2,1,1,1,0,0,0,0,0,0,0]))
print(solution(1,	[1,0,0,0,0,0,0,0,0,0,0]	))
print(solution(9,	[0,0,1,2,0,1,1,1,1,1,1]))
print(solution(10,	[0,0,0,0,0,0,0,0,3,4,3]))