def is_paired(input_string):
    if input_string is None:
        return True
    l_brackets = ["[", "{", "("]
    r_brackets = ["]", "}", ")"]
    stack = []
    for elt in input_string:
        if elt in l_brackets:
            stack.append(elt)
        elif elt in r_brackets:
            if not stack or l_brackets[r_brackets.index(elt)] != stack.pop():
                return False
    return len(stack) == 0
