def grid(a, b):
    for i in range(11):
        if i == 0 or i == 5 or i == 10:
            for j in range (11):
                if j == 0 or j == 5 or j == 10:
                    print(a, '', end='')
                else: print(b, '', end='')
            print()
        else:
            print('|', ' ' * 7, '|', ' ' * 7, '|')


grid('#', '_')