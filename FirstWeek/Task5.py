num_list = [10, 2, 3, 4, 5, 6, 7, 82, 9, 10, 11, 12, 13, 14, 15, 16]
w_size = 1
i_stack = []
o_stack = []
ind_mul = 1
ind = 0


def add_with_max(num: int, destiny: list):
    """stack with maximum"""
    if len(destiny) == 0:
        destiny.append([num, num])
        return
    destiny.append([num, num if num > destiny[-1][1] else destiny[-1][1]])


def i_stack_fill(i_stack: list):
    """filling stack with maximum"""
    for i in range(w_size * (ind_mul - 1), w_size * ind_mul):
        add_with_max(num_list[i], i_stack)


def o_stack_fill(o_stack: list):
    """reverse i_stack with maximum"""
    for i in range(w_size):
        add_with_max(i_stack[-1][0], o_stack)
        i_stack.pop()


def get_max(i_stack: list, o_stack: list):
    """get max even if we get index range error"""
    if not len(o_stack):
        return i_stack[-1][1]

    if not len(i_stack):
        return o_stack[-1][1]

    return max(i_stack[-1][1], o_stack[-1][1])


def add_inp_pop_out(i_stack: list, o_stack: list):
    """adding with max and popping from stacks"""
    global ind

    if not len(o_stack):
        return

    if ind >= len(num_list) and len(o_stack):
        o_stack.pop()
        return

    add_with_max(num_list[ind], i_stack)
    o_stack.pop()
    ind += 1


while ind < len(num_list):
    if not len(i_stack):
        i_stack_fill(i_stack)
    if not len(o_stack):
        o_stack_fill(o_stack)
    if not ind:
        print(get_max(i_stack, o_stack), end=' ')
    ind_mul += 1
    ind = w_size * (ind_mul - 1)
    while len(i_stack) + len(o_stack) == w_size and len(i_stack) < w_size:
        add_inp_pop_out(i_stack, o_stack)
        if len(i_stack) + len(o_stack) == w_size:
            print(get_max(i_stack, o_stack), end=' ')




