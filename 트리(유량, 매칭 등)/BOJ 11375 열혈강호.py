import sys

def main():
    def dfs(visit, node):
        if visit[node] == 1:
            return 0

        visit[node] = 1

        for key in employee[node]:
            if ans[key] == 0:
                ans[key] = node
                return 1

        for key in employee[node]:
            if dfs(visit, ans[key]):
                ans[key] = node
                return 1

        return 0

    n, m = map(int, sys.stdin.readline().split())
    employee, ans = [[] for _ in range(n + 1)], [0] * (m + 1)

    for i in range(1, n + 1):
        temp = list(map(int, sys.stdin.readline().split()))
        for item in temp[1:]:
            employee[i].append(item)

    cnt = 0
    for i in range(1, n + 1):
        visit = [0] * (n + 1)
        if dfs(visit, i):
            cnt += 1

        if cnt == m:
            break

    print(cnt)

if __name__=="__main__":
    main()