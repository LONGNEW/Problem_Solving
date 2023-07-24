def solution(k, dungeons):
    def dfs(data, visit, fatigue, did):
        temp = did

        for i in range(len(data)):
            if visit[i] == 1:
                continue

            need, spend = data[i]
            if fatigue >= need:
                visit[i] = 1
                temp = max(temp, dfs(data, visit, fatigue - spend, did + 1))
                visit[i] = 0
        return temp

    visit = dict()
    for i in range(len(dungeons)):
        visit[i] = 0
    return dfs(dungeons, visit, k, 0)