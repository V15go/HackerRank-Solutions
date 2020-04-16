n=int(input())
cl = [int(x) for x in input().split()][:n]
cl=list(set(cl))
cl.sort()

cl.remove(max(cl))
print(cl[-1])