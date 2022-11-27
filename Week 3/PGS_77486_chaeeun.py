def solution(enroll, referral, seller, amount):
    global profit
    global parent
    profit = { en: 0 for en in enroll }
    parent = {}
    for i in range(len(enroll)):
        parent[enroll[i]] = referral[i]
    for i in range(len(seller)):
        solve(seller[i], amount[i] * 100)
    answer = list(profit.values())
    return answer

def solve(child, money):
    global parent
    global profit
    if child == '-' or money == 0:
        return
    p_money = int(money * 0.1)
    profit[child] += money - p_money
    solve(parent[child], p_money)
