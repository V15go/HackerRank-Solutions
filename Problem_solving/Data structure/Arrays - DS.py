n=int(input())
arr=list(map(int, input().split()))[:n]
print(" ".join(str(x) for x in reversed(arr)))