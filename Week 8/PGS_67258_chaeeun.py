def solution(gems):
    answer = [1, len(gems)]
    _min = len(gems) + 1
    sp, ep = 0, 0
    kind = len(set(gems))
    visit = dict()
    
    while ep < len(gems):
        if gems[ep] not in visit:
            visit[gems[ep]] = 1
        else:
            visit[gems[ep]] += 1
        ep += 1
        
        if len(visit) == kind:
            while sp < ep:
                if visit[gems[sp]] > 1:
                    visit[gems[sp]] -= 1
                    sp += 1
                elif _min > ep - sp:
                    _min = ep - sp
                    answer = [sp + 1, ep]
                    break
                else:
                    break
                
    return answer