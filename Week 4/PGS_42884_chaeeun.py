def solution(routes):
    answer = 0
    routes.sort(key = lambda x: (x[0], x[1]))
    cur = -30001
    for (s, e) in routes:
        if cur < s:
            cur = e
            answer += 1
        if cur > e:
            cur = e
    return answer