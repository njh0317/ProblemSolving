from heapq import heappush, heappop
def solution(n, works):
    heap = []
    
    for w in works:
        heappush(heap, (-w, w))
    print(heap)
    answer = 0
    
    for i in range(n):
        if(heap[0][1] == 0): break
        newWork = heappop(heap)[1]-1
        heappush(heap, (-newWork, newWork))
    
    for pri, value in heap:
        answer+=value**2
        
    return answer