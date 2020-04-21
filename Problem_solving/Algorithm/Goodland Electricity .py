n, k = map(int, input().split())
a = list(map(int, input().split()))
i, j, trans, flag, loc = 0, 0, 0, 0, 0
while(i<n):
    trans += 1
    j = i+k-1
    if j > n:
        j = n-1
    while loc <= j <n and a[j]==0:
        j -= 1
    if j < loc:
        print(-1)
        flag = 1
        break
    else:
        loc = j+1
        j += k
        i = j
if flag == 0:
    print(trans)





