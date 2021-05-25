import sys

data = sys.stdin.readline().rstrip()
ans = []
temp = []
operator = {"*":2, "/":2, "+":1, "-":1, "(":0}

for item in data:
    if 'A' <= item <= 'Z':
        ans.append(item)
    elif item == '(':
        temp.append(item)
    elif item == ')':
        while temp[-1] != '(':
            ans.append(temp.pop())
        temp.pop()
    else:
        while len(temp) > 0 and operator[item] <= operator[temp[-1]]:
            ans.append(temp.pop())
        temp.append(item)

while temp:
    ans.append(temp.pop())
print("".join(ans))