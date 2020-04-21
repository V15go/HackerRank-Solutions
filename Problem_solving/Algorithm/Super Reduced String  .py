a = input()
ans =[]
for i in a:
    if ans and ans[-1]==i:
        ans.pop()
    else:
        ans.append(i)

if len(ans)==0:
    print("Empty String")
else:
    print(''.join(ans))




