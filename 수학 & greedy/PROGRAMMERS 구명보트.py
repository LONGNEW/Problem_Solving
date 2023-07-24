def solution(people, limit):
    people.sort()
    l, r = 0, len(people) - 1

    cnt = 0
    while l <= r:
        cnt += 1
        lval, rval = people[l], people[r]
        if lval + rval <= limit:
            l += 1
        r -= 1

    return cnt