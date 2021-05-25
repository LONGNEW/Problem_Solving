import sys

n = int(sys.stdin.readline())
graph = [[-1, -1] for i in range(n)]

def print_node(start):
    print(chr(start + 65), end="")
    if graph[start][0] != -1:
        print_node(graph[start][0])
    if graph[start][1] != -1:
        print_node(graph[start][1])

def print_middle_dfs(start):
    if graph[start][0] != -1:
        print_middle_dfs(graph[start][0])
    print(chr(start + 65), end="")
    if graph[start][1] != -1:
        print_middle_dfs(graph[start][1])

def print_after_dfs(start):
    if graph[start][0] != -1:
        print_after_dfs(graph[start][0])
    if graph[start][1] != -1:
        print_after_dfs(graph[start][1])
    print(chr(start + 65), end="")

for i in range(n):
    a, b, c = sys.stdin.readline().split()
    idx = ord(a) - 65
    if b != '.':
        graph[idx][0] = ord(b) - 65
    if c != '.':
        graph[idx][1] = ord(c) - 65

print_node(0)
print()
print_middle_dfs(0)
print()
print_after_dfs(0)