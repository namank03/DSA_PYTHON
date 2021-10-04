# Python program to validate if the expression is correct or not via stack

#  Ex -  [(5*9) + (7*9)]  - valid expression
#  Ex -  [(5*9 + (7*9)]  - Invalid expression

# Algorithm steps
# 1. check for "[{()}]"
# 2. move "[{(" in the stack
# 3. whenever the next expression is in and ")}]" pop the value from stack and compare
# 4. If the value does not match the expression is invalid - print and exit the program
# 5. If the iteration is done and the stack is not empty - expression is not valid - print and exit the program
# 6. else if the stack is empty - expression is not valid - print and exit the program

import sys


# expression = input("Enter the expression\n")
def expression_test(expression):
    stack = []
    push_dict = {'[': 0, '{': 1, '(': 2}
    pop_dict = {']': 0, '}': 1, ')': 2}
    for i in expression:
        if i != ' ':
            if i in push_dict:
                stack.append(i)
            if i in pop_dict:
                try:
                    popped_element = stack.pop()
                except IndexError:
                    print("Invalid expression")
                    return
                if push_dict[popped_element] != pop_dict[i]:
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
