def expression_test(expression):
    stack = []
    exp_dict = {'[': ']', '{': '}', '(': ')'}
    for i in expression:
        if i != ' ':
            if i in exp_dict.keys():
                stack.append(i)
            if i in exp_dict.values():
                try:
                    popped_element = stack.pop()
                except IndexError:
                    print("Invalid expression")
                    return
                if exp_dict[popped_element] != i:
                    print('Expression Invalid')
                    return

    if len(stack) > 0:
        print("Expression Invalid")
    else:
        print("Expression Valid")


if __name__ == "__main__":
    expression_list = ["[({)}", '{([]))', "{{{}}}", "[{()})", "[{()}]"]
    for expression in expression_list:
        expression_test(expression)
