def right_justify(s):
    for i in range(71):
        tot = 71 - len(s)
        if i < tot:
            print(f'{i}', end=' ')
    for j in range(len(s)):
        print(f'{s[j]}', end= ' ')


right_justify('A')