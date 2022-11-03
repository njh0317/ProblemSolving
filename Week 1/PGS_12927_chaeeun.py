import heapq
def solution(n, works):
    answer = 0
    h = list(map(lambda x: x*(-1), works))
    heapq.heapify(h)

    for _ in range(n):
        w = heapq.heappop(h)
        if w == 0:
            break
        heapq.heappush(h, w + 1)

    for w in h:
        answer += w*w

    return answer