n, m = map(int, input().split())
a = list(map(int, input().split()))[:n]
b = set(map(int, input().split()))
c = set(map(int, input().split()))
d = 0
for i in range(n):
    if a[i] in b:
        d = d + 1
    elif a[i] in c:
        d = d - 1

print(d)