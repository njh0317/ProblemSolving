track = {}
def dfs(leftTicket, answer, start, visited):
    if(leftTicket == 0):
        return answer
    if(start not in track.keys()): return []
    possible = track[start]
    possible.sort()
    
    for end in possible:
        if(start+end in visited.keys() and visited[start+end] > 0):
            answer.append(end)
            visited[start+end]-=1
            temp = dfs(leftTicket-1, answer, end, visited)
            if(temp != []) : return temp
            visited[start+end]+=1
            answer.pop(-1)   
    return []
def solution(tickets):
    answer = []
    totalTicketNum = len(tickets)
    visited = {}
    for a, b in tickets:
        if(a in track.keys()) :
            track[a].append(b)
        else:
            track[a] = [b]
        if(a+b in visited.keys()) :
            visited[a+b]+=1
        else:
            visited[a+b] = 1
    for key in track.keys():
        track[key].sort()
    answer = dfs(totalTicketNum, ["ICN"], "ICN", visited)
    return answer
