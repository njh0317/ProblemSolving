def solution(a, b):
    s = 0
    
    if a >= b:
        n_l = a
        n_s = b
        
    else:
        n_l = b
        n_s = a
        
    for i in range(n_s, n_l+1):
        s += i