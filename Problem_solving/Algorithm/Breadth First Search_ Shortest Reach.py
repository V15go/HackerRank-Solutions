from collections import defaultdict
def Build(n,m):
    graph= defaultdict(list)

    while m>0:
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
        m -=1
    return graph
def cal(s, graph):
    distances = {s: 0}
    queue = []
    queue.append(s)
    while queue:
        sa = queue.pop(0)
        dis = distances[sa] + 6
        for i in graph[sa]:
            if i in distances:
                continue
            distances[i] = dis
            queue.append(i)
    return distances

for t in range(int(input())):
    n,m = map(int, input().split())
    graph = Build(n,m)
    s = int(input())
    distances = cal(s, graph)
    for i in range(1, n + 1):
        if (i == s):
            continue
        if i in distances:
            print(distances[i], end=" "),
        else:
            print(-1, end=" "),
    print()




