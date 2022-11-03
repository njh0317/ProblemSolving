def solution(s1, s2):
    answer = 0

    for st2 in s2:
        for st1 in s1:
            if st1 == st2:
                answer += 1

    return answer