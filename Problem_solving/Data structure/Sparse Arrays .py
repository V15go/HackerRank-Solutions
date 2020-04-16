
def hg(arr):
    mas=-63
    for i in range(4):
        for j in range(4):
            top = sum(arr[i][j:j+3])
            mid=arr[i+1][j+1]
            bottom=sum(arr[i+2][j:j+3])
            hd=top+mid+bottom
            if hd > mas:
                mas=hd
    return mas
arr = []
for _ in range(6):
    arr.append(list(map(int, input().split())))
print(hg(arr))