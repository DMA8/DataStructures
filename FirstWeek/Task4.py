a = int(input())
"""в случае пуша, мы добавляем число в стек. вычисляем максимальное и добавляем его в другой стек"""
comm = []
for i in range(a):
    comm.append(input().split())
def stack_with_max(commands:list):
    stack = []
    maximum = []
    for i in commands:
        if i[0] == 'push':
            i[1] = int(i[1])
            stack.append(i[1])
            if not len(maximum):
                maximum.append(i[1])
            else:
                if i[1] >= maximum[-1]:
                    maximum.append(int(i[1]))
                else:
                    maximum.append(maximum[-1])
        elif i[0] == 'max':
            print(maximum[-1])
        elif i[0] == 'pop':
            stack.pop()
            maximum.pop()
stack_with_max(comm)