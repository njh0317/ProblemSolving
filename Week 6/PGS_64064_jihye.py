import copy
answer = []
def check_expression(uid, exp): #id 가 exp에 해당하는지 boolean return
    if(len(uid)!=len(exp)):
        return False
    for index in range(len(uid)):
        if(exp[index]=='*'):
            continue
        if(uid[index]!=exp[index]):
            return False
    return True
def backtracking(index, banned_id, dic, choose_list):
    global answer
    if(index == len(banned_id)):
        temp = copy.deepcopy(choose_list)
        temp.sort()
        if temp not in answer:
            answer.append(temp)
        return
    for uid in dic[banned_id[index]]:
        
        if(uid not in choose_list):
            choose_list.append(uid)
            backtracking(index+1, banned_id, dic, choose_list)
            choose_list.pop(-1)
    return
def solution(user_id, banned_id):
    global answer
    answer = []
    dic = {} #key = banned_id, value = banned_id에 해당될 수 있는 user_id 리스트
    for banned in banned_id: 
        new_value = []
        for uid in user_id:
            if(check_expression(uid, banned)):
                new_value.append(uid)
        dic[banned] = new_value
    backtracking(0, banned_id, dic, [])
    return len(answer)