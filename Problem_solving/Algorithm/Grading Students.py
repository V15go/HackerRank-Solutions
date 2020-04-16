s,t=map(int,input().split())
a,b=map(int,input().split())
m,n=map(int,input().split())
lisa=(map(int,input().split()))
lisb=(map(int,input().split()))
app=0
ora=0
for i in lisa:
    if s <= i+a <= t:
        app+=1

print(app)
for i in lisb:
    if s <= i+b <= t:
        ora+=1
print(ora)