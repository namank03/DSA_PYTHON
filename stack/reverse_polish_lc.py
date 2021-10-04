from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        operators = ['*', '**', '+', '-', '/']

        for i in tokens:
            if i not in operators:
                stack.append(i)
            else:
                right = stack.pop()
                left = stack.pop()
                string = left + i + right
                # * TIP: converting float to int will truncate the float towards 0 from both the side's of the number line
                string = str(int(eval(string)))
                stack.append(string)

        return stack.pop()
