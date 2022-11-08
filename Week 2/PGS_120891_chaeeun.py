def solution(order):
    answer = 0
    for o in str(order):
        if o != '0' and int(o) % 3 == 0:
            answer += 1
    return answer