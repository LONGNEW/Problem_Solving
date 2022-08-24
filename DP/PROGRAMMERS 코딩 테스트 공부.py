def solution(alp, cop, problems):
    req_alp, req_cop = -1, -1
    for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
        req_alp = max(req_alp, alp_req)
        req_cop = max(req_cop, cop_req)

    problems.append([0, 0, 1, 0, 1])
    problems.append([0, 0, 0, 1, 1])

    dp = [[float("inf")] * (req_cop + 1) for _ in range(req_alp + 1)]
    alp, cop = min(alp, req_alp), min(cop, req_cop)
    dp[alp][cop] = 0

    for x in range(alp, req_alp + 1):
        for y in range(cop, req_cop + 1):

            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                dx, dy = min(x + alp_rwd, req_alp), min(y + cop_rwd, req_cop)
                if x < alp_req or y < cop_req:
                    continue
                dp[dx][dy] = min(dp[dx][dy], dp[x][y] + cost)

    return dp[req_alp][req_cop]

print(solution(10, 10, [[10,15,2,1,2],[20,20,3,3,4]]))
print(solution(0, 0, [[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]]))