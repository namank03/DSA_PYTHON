intervals = [
    [1, 5],
    [3, 7],
    [4, 6],
    [6, 8],
    [9, 12],
    [10, 13],
    [15, 20],
]

# intervals = sorted(intervals, key=lambda x: x[0])

new_intervals = [intervals[0][:]]


def merge_interval(intervals):
    for i in range(1, len(intervals)):
        # possible merge
        if new_intervals[-1][1] >= intervals[i][0]:
            new_intervals[-1][1] = max(new_intervals[-1][1], intervals[i][1])
        else:
            new_intervals.append(intervals[i][:])


merge_interval(intervals)
