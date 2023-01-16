# 대문자와 소문자

def solution(my_string):
    l = []
    for s in my_string:
        if 'a' <= s <= 'z':
            l.append(s.upper())
        elif 'A' <= s <= 'Z':
            l.append(s.lower())
    
    answer = ''.join(l)
    return answer