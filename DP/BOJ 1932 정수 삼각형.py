n = int(input())
triangle = []
answer = []

for i in range(n):
    data = list(map(int, input().split()))
    for j in range(len(data)):
        triangle.append(data[j])
        answer.append(data[j])
        
find_child_idx = 0
for gap in range(1, n):
    for _ in range(gap):
        left_child_idx = find_child_idx + gap
        right_child_idx = find_child_idx + gap + 1
        
        answer[left_child_idx] = max(answer[left_child_idx], triangle[left_child_idx] + answer[find_child_idx])
        answer[right_child_idx] = max(answer[right_child_idx], triangle[right_child_idx] + answer[find_child_idx])
        
        find_child_idx += 1
        
print(max(answer))