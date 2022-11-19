def solution(n):
    answer = 0
    half = n ** (1/2)
    for i in range(1, int(half) + 1):
        if n % i == 0:
            answer += (i + n //i) if i != n//i else i
    return answer