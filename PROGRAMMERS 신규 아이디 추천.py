def solution(new_id):
    # 1단계
    new_id = new_id.lower()

    # 2단계
    temp = ""
    for item in new_id:
        if item in "abcdefghijklmnopqrstuvwxyz0123456789-_.":
            temp += item
    new_id = temp
    print(new_id)

    # 3단계
    temp, cnt = "", 0
    for item in new_id:
        if item == ".":
            cnt += 1
            continue

        if cnt > 0 and item != ".":
            cnt = 0
            temp += "."

        temp += item
    if cnt > 0:
        temp += "."
    new_id = temp
    print(new_id)

    # 4단계
    if new_id and new_id[0] == ".":
        new_id = new_id[1:]
    if new_id and new_id[-1] == ".":
        new_id = new_id[:-1]
    print(new_id)

    # 5단계
    if len(new_id) == 0:
        new_id = "a"
    print(new_id)

    # 6단계
    if len(new_id) >= 16:
        new_id = new_id[:15]
        print(f"변경된 길이 : {len(new_id)}")

        if new_id[-1] == ".":
            new_id = new_id[:-1]

            # 7단계
    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id += new_id[-1]
    return new_id