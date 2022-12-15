def solution(tickets):
    answer = None
    tickets.sort(key = lambda x: ( x[1], x[0]) )
    for i in range(len(tickets)):
        if tickets[i][0] == "ICN":
            visit = [False] * len(tickets)
            visit[i] = True
            answer = dfs(tickets, visit, i, [tickets[i][0], tickets[i][1]])
            if answer != None:
                return answer

def dfs(tickets, visit, cur, result):
    if False not in visit:
        return result
    for i in range(len(tickets)):
        if visit[i] == False and tickets[cur][1] == tickets[i][0]:
            visit[i] = True
            result.append(tickets[i][1])
            temp = dfs(tickets, visit, i, result)
            if temp != None:
                return temp
            result.pop()
            visit[i] = False
    return None