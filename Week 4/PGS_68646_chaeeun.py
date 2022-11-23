def solution(a):
    answer = 2
    _min = min(a)
    base = a.index(_min)
    if base not in [0, len(a) -1]:
        answer += 1
    
    # 내 오른쪽에 이미 작은 값 있음. 내 왼쪽에 나보다 작은 값이 있으면 안 됨
    low = 1000000000
    for i in range(1, base):
        low = min(low, a[i - 1])
        if low > a[i]:
            answer += 1

    # 내 왼쪽에 이미 작은 값 있음. 내 오른쪽에 나보다 작은 값이 있으면 안 됨
    low = 1000000000
    for i in range(len(a) - 2, base, -1):
        low = min(low, a[i + 1])
        if a[i] < low:
            answer += 1

    return answer