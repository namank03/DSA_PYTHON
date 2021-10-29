class Solution:
    def numDecodings(self, s: str) -> int:

        # Edge cases
        if s == "0" or s.startswith('0'):
            return 0

        @lru_cache(maxsize=None)
        def solve(a, i):

            # base case 1
            if i in [0, 1]:
                return 1

            # base case 2
            if i < 0:
                return

            # We've 2 options here either to take one last element  or to take 2 last elements.
            op1 = a[i-1]
            op2 = a[i-2] + a[i-1]

            # Initialize the solution count to 0
            count = 0

            # checking if op2 is valid? If yes, then we can drop the last 2 letters.
            if not (op2.startswith('0') or int(op2) > 26):
                count += solve(a, i-2)

            # Check if op1 is valid?
            if not op1.startswith('0'):
                count += solve(a, i-1)

            # Return the final count
            return count

        return solve(s, len(s))
