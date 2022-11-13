def solution(order):
    a = str(order)
    cnt = 0
    
    for i in range(len(a)):
        if int(a[i]) % 3 == 0 and int(a[i]) != 0:
            cnt += 1
    return cnt