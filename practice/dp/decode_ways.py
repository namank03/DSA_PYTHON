
from visualiser.visualiser import Visualiser as vs


def decode_ways(s):

    @vs(node_properties_kwargs={"shape": "record", "color": "#f57542", "style": "filled", "fillcolor": "grey"})
    def dp(s):
        # * basecase for the invalid condition
        if len(s) > 1 and s[0] == '0':
            return 0

        # * this will cover the base of case of both n+2, n+1
        if len(s) in [0, 1]:
            return 1

        # if the string is in valid range we've 2 choice to pick from
        if int(s[:2]) < 27:
            return dp(s[1:]) + dp(s[2:])
        # If invalid, then we can only pick 1 digit number
        else:
            return dp(s[1:])

    return dp(s)


print(decode_ways('226'))
vs.make_animation("images/decode_ways.gif", delay=2)
