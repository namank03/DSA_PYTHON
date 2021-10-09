from visualiser.visualiser import Visualiser as vs


@vs(node_properties_kwargs={"shape": "record", "color": "#f57542", "style": "filled", "fillcolor": "grey"})
def best_sum_length(arr, target, n):

    if target == 0:
        return 1

    if n == 0:
        return 0

    if target >= arr[n-1]:
        return 1 + min(
            best_sum_length(arr, target - arr[n-1], n),
            best_sum_length(arr, target, n - 1)
        )
    else:
        return best_sum_length(arr, target, n - 1)


def main():
    # Call function
    best_sum_length([2, 1], 5, 2)
    # Save recursion tree to a file
    vs.make_animation("best_sum_length.gif", delay=2)


if __name__ == "__main__":
    main()
