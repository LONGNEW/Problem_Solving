def solution(enroll, referral, seller, amount):
    answer = []
    parent, total = dict(), dict()

    for i in range(len(enroll)):
        item, parent_item = enroll[i], referral[i]
        parent[item] = parent_item
        total[item] = 0

    def dfs(node, money):
        if node == "-":
            return

        for_parent = money * 0.1
        total[node] += money

        if for_parent >= 1:
            # parent에 분배금을 주지도 않는 경우를 따져
            # 시간복잡도에서 이득을 보기
            for_parent = int(for_parent)
            total[node] -= for_parent
            dfs(parent[node], for_parent)

    for i in range(len(seller)):
        item, profit = seller[i], amount[i] * 100
        dfs(item, profit)

    for key in parent.keys():
        answer.append(total[key])
    return answer