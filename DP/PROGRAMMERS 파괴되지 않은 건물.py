def solution(board, skill):
    m, n = len(board[0]), len(board)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for type, r1, c1, r2, c2, degree in skill:
        degree = -degree if type == 1 else degree

        dp[r1][c1] += degree
        dp[r2 + 1][c1] -= degree
        dp[r1][c2 + 1] -= degree
        dp[r2 + 1][c2 + 1] += degree

    for x in range(n + 1):
        for y in range(1, m + 1):
            dp[x][y] += dp[x][y - 1]

    for y in range(m + 1):
        for x in range(1, n + 1):
            dp[x][y] += dp[x - 1][y]

    cnt = 0
    for x in range(n):
        for y in range(m):
            if board[x][y] + dp[x][y] > 0:
                cnt += 1

    return cnt

print(solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]],	[[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]))
print(solution([[1,2,3],[4,5,6],[7,8,9]],	[[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]))