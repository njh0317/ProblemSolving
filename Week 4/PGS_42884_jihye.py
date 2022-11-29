def solution(routes):
    answer = 0

    routes.sort(key = lambda x: (x[0], x[1]))

    index = 0

    while(index < len(routes)):
        start, end = routes[index]
        find_index = index
        for i in range(index+1, len(routes)):
            next_start, next_end = routes[i]
            if(next_start<=end):
                find_index = i
                end = min(end, next_end)
            else:
                break
        answer+=1
        if(find_index == index):
            index+=1
        else:
            index = find_index+1
    return answer