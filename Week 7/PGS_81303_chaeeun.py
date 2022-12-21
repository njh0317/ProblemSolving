
N = 0
class Node:
    live = True
    def __init__(self, p, n):
        self.prev = p if p >= 0 else None
        self.next = n if n < N else None

def solution(n, k, cmd):
    global N
    N = n
    table = {i : Node(i-1, i+1) for i in range(n)}
    removed = []

    for c in cmd:
        if c[0] == 'U':
            for _ in range(int(c.split()[1])):
                k = table[k].prev
        elif c[0] == 'D':
            for _ in range(int(c.split()[1])):
                k = table[k].next
        elif c[0] == 'C':
            table[k].live = False            
            removed.append(k)
            prev, next = table[k].prev, table[k].next
            if prev is not None:
                table[prev].next = table[k].next
            if next is not None:
                table[next].prev = table[k].prev
            if table[k].next is None:
                k = table[k].prev
            else:
                k = table[k].next

        elif c[0] == 'Z':
            recover = removed.pop()
            table[recover].live = True
            prev, next = table[recover].prev, table[recover].next
            if prev is not None:
                table[prev].next = recover
            if next is not None:
                table[next].prev = recover
    answer = ''
    for i in range(n):
        answer += 'O' if table[i].live else 'X'
    return answer
            