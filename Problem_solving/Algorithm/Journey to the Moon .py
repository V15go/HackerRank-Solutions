n=int(input())
for i in range(n):
    lis=int(input().strip())

    if lis>=38 and lis%5>=3:
        while lis%5 != 0:
            lis+=1
    print(lis)