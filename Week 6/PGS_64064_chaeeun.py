result = []
def solution(user_id, banned_id):
    global result
    used_user = [False] * len(user_id)
    used_ban = [False] * len(banned_id)
    dfs(0, 0, user_id, banned_id, used_user, used_ban, [])
    return len(result)

def dfs(idx_i, idx_j, user_id, banned_id, used_user, used_ban, dup):
    global result
    if False not in used_ban:
        # print(dup)
        if sorted(dup) not in result:
            result.append(sorted(dup))
        # print(result)
        return
    for i in range(idx_i, len(banned_id)):
        if used_ban[i] == True:
            continue
        for j in range(idx_j, len(user_id)):
            if used_user[j] == True:
                continue
            if is_duplicated(user_id[j], banned_id[i]) == True:
                used_ban[i] = True
                used_user[j] = True
                dup.append(user_id[j])
                dfs(i+1, 0, user_id, banned_id, used_user, used_ban, dup)
                dup.pop()
                used_ban[i] = False
                used_user[j] = False
    return
       
def is_duplicated(uid, bid):
    if len(uid) != len(bid):
        return False
    for i in range(len(uid)):
        if bid[i] == '*':
            continue
        if uid[i] != bid[i]:
            return False
    return True