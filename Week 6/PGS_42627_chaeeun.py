from heapq import heappush, heappop

def solution(jobs):
    answer, done, now, pre = 0, 0, 0, -1
    h = []
    
    while done < len(jobs):
        for job in jobs:
            if pre < job[0] <= now:
                heappush(h, [job[1], job[0]])
        if len(h):
            job = heappop(h)
            answer += now + job[0] - job[1]
            pre = now
            now += job[0]
            done += 1
        else: 
            now += 1
    return int(answer / len(jobs))