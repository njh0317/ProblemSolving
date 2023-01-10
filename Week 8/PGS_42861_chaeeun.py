def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else: 
        parent[a] = b

def solution(n, costs):
    answer = 0
    parent = dict()
    for cost in costs:
        parent[cost[0]] = cost[0]
        parent[cost[1]] = cost[1]
    costs.sort(key = lambda x: x[2])
    for c in costs:
        if find_parent(parent, c[0]) == find_parent(parent, c[1]):
            continue
        else:
            answer += c[2]
            union_parent(parent, c[0], c[1])
    return answer