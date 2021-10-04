class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        exp_dict = {'[': ']', '{': '}', '(': ')'}
        for i in s:
            if i != ' ':
                if i in exp_dict:
                    stack.append(i)
                if i in exp_dict.values():
                    try:
                        popped_element = stack.pop()
                    except IndexError:
                        return False
                    if exp_dict[popped_element] != i:
                        print('s Invalid')
                        return False

        return len(stack) <= 0
