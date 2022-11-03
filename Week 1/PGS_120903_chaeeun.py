def solution(s1, s2):
    answer = 0
    
    for w in s1:
        if w in s2:
            answer += 1
        
    return answer