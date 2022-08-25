import math

def solution(fees, records):
    enter, tot_min = dict(), dict()

    def_min, def_fee, unit_min, unit_fee = fees
    for item in records:
        time, num, behavior = item.split(" ")
        hour, min = map(int, time.split(":"))

        if num not in tot_min:
            tot_min[num] = 0

        if behavior == "IN":
            enter[num] = hour * 60 + min
        else:
            now = hour * 60 + min
            tot_min[num] += now - enter[num]
            del enter[num]

    for key in enter.keys():
        now = 23 * 60 + 59
        tot_min[key] += now - enter[key]

    temp_ans = []
    for key in tot_min.keys():
        total = tot_min[key]

        if def_min >= total:
            temp_ans.append((key, def_fee))
        else:
            times = math.ceil((total - def_min) / unit_min)
            temp_ans.append((key, def_fee + unit_fee * times))

    temp_ans.sort()
    ans = [fee for _, fee in temp_ans]

    return ans
