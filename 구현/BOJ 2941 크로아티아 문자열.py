import sys

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
data = sys.stdin.readline().strip()
for item in croatia:
    data = data.replace(item, 'a')
print(len(data))