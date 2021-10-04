# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.


# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]

# !Algorithm: Here the idea is to use "monotonically decreasing" stack.
# The stack will hold the index/temperature and whenever the temperature with greater values occurs, the pop operator will kick in and the difference between the index will give the result.


from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        days = [0] * len(temperatures)
        stack = []
        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                _, init_index = stack.pop()
                days[init_index] = index - init_index
            stack.append((temp, index))
        return days
