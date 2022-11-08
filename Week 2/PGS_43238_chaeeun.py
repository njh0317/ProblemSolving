def solution(n, times):
    answer = 0
    _min = min(times)
    _max = max(times) * n
    
    while True:
        mid = (_min + _max) // 2
        if _min == _max:
            break
        tmp = 0
        for t in times:
            tmp += mid // t
        if tmp >= n:
            answer = mid
            _max = mid
        else:
            _min = mid + 1
        
    return answer


# def solution(n, times):
#     answer = 0
#     arr = []
#     for t in times:
#         for i in range(1, n + 1):
#             arr.append(i * t)
#     answer = sorted(arr)[n - 1]
#     return answer