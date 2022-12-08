def solution(s):
    if len(s) != 4 and len(s) != 6:
        return False
    for x in s:
        if x.isalpha():
            return False
    return True