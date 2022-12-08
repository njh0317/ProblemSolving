def solution(price, money, count):
    value = price * int(count * (count + 1) // 2)
    answer = 0 if value < money else value - money
    return answer