n = int(input())
lis = list(map(int, input().split()))[:n]
a = set(lis)
i = 0
while len(a) > 0:
    i += 1
    m = min(a)
    a = list(filter(lambda x: x > m+4, a))
print(i)




