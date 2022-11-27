from collections import deque
def solution(n, edge):
    answer = 0
    graph = []
    for i in range(n + 1):
        graph.append([])
    for e in edge:
        graph[e[0]] += [e[1]]
        graph[e[1]] += [e[0]]
    visited = [-1] * (n + 1)
    bfs(graph, visited)
    answer = visited.count(max(visited))
    return answer

def bfs(graph, visited):
    q = deque([1])
    visited[1] = 0
    while q:
        cur = q.popleft()
        for v in graph[cur]:
            if visited[v] == -1:
                q.append(v)
                visited[v] = visited[cur] + 1
