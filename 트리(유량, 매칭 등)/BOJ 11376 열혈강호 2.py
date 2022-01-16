import sys

def main():
    def dfs(node):
        if visit[node] == 1:
            return 0

        visit[node] = 1

        for key in employee[node]:
            if ans[key] == 0:
                ans[key] = node
                return 1

        for key in employee[node]:
            if dfs(ans[key]):
                ans[key] = node
                return 1

        return 0

    n, m = map(int, sys.stdin.readline().split())
    employee, ans = [[] for _ in range(n + 1)], [0] * (m + 1)

    for i in range(1, n + 1):
        temp = list(map(int, sys.stdin.readline().split()))
        employee[i] += temp[1:]

    cnt = 0
    for _ in range(2):
        for i in range(n + 1):
            if cnt == m:
                break

            visit = [0] * (n + 1)
            if dfs(i):
                cnt += 1

    print(cnt)

if __name__ == '__main__':
    main()