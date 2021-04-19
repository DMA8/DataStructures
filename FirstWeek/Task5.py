a = input()
seq = [int(i) for i in input().split()]
win_size = int(input())
ans = []
if win_size == 1:
    for i in seq:
        print(i, end=' ')
else:
    stack_inp = [[0, 0]]
    stack_out = [[0, 0]]
    for i in range(win_size):  # добавляем в стек с поддержкой максимума
        stack_inp.append([seq[i], seq[i] if seq[i] > stack_inp[-1][1] else stack_inp[-1][1]])
    for i in range(win_size):  # пересыпаем из одного стека в другой (очередь)
        stack_out.append(
            [stack_inp[-1][0], stack_inp[-1][0] if stack_inp[-1][0] > stack_out[-1][1] else stack_out[-1][1]])
        stack_inp.pop()
    flag = 1
    print(stack_out[-1][1], end=' ')
    ans.append(stack_out[-1][1])
    for i in range(win_size, len(seq)):
        if len(stack_out)>1 and flag:
            stack_inp.append([seq[i], seq[i] if seq[i] > stack_inp[-1][1] else stack_inp[-1][1]])
            stack_out.pop()
            a = max(stack_inp[-1][1], stack_out[-1][1])
            ans.append(a)
            print(max(stack_inp[-1][1], stack_out[-1][1]), end=' ')
            if len(stack_out) == 1:
                flag = 0
        elif len(stack_inp)>1 and not flag:
            for i in range(win_size):  # пересыпаем из одного стека в другой (очередь)
                stack_out.append(
                    [stack_inp[-1][0], stack_inp[-1][0] if stack_inp[-1][0] > stack_out[-1][1] else stack_out[-1][1]])
                stack_inp.pop()
            if len(stack_inp) == 1: flag = 1
        else:
            flag = 1
            stack_out.pop()
            print(max(stack_inp[-1][1], stack_out[-1][1]), end='')
            print()
            ans.append(max(stack_inp[-1][1], stack_out[-1][1]))
