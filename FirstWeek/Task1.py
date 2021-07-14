a = input()
def check_bracket_sequence(brackets):
    bracket_pairs = {'(': ')', '[': ']', '{': '}'}
    _stack = []
    _index_to_save = []
    if len(brackets) == 1:
        return 1
    for i in range(len(brackets)):
        if brackets[i] not in bracket_pairs and brackets[i] not in bracket_pairs.values():
            continue
        if brackets[i] in bracket_pairs:
            _stack.append(brackets[i])
            _index_to_save.append(i)
        elif len(_stack) > 0 and brackets[i] == bracket_pairs[_stack[-1]]:
            _stack.pop()
            _index_to_save.pop()
        else:
            return i+1
    if not len(_stack):
        return 'Success'
    else:
        return _index_to_save[-1] + 1
print(check_bracket_sequence(a))