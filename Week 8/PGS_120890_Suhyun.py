def solution(array, n):
    l = []
    for i in range(len(array)):
        l.append((array[i], abs(array[i]-n)))

    l.sort(key = lambda x: (x[1], x[0]))
    answer = l[0][0]
    return answer