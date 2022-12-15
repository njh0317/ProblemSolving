def solution(price, money, count):
    new_p = 0
    price_n = 0
    
    for i in range(1, count+1):
        price_n = price * i
        new_p += price_n
    
    if money < new_p:
        answer = new_p - money
    else:
        answer = 0

    return answer