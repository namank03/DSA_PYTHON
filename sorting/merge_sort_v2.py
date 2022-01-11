def merge(arr, L, R):
    i = j = 0
    op = []
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            op.append(L[i])
            i += 1
        else:
            op.append(R[j])
            j += 1

    while i < len(L):
        op.append(L[i])
        i += 1

    while j < len(R):
        op.append(R[j])
        j += 1

    return op


from visualiser.visualiser import Visualiser as vs


@vs(
    node_properties_kwargs={
        "shape": "record",
        "color": "#f57542",
        "style": "filled",
        "fillcolor": "grey",
    }
)
def mergeSort(arr):
    if len(arr) <= 1:
        return

    mid = len(arr) // 2
    L = arr[:mid]
    R = arr[mid:]
    mergeSort(L)
    mergeSort(R)
    return merge(arr, L, R)


# Code to print the list


# Driver Code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    mergeSort(arr)
    print(f'arr -> {arr}')
    vs.make_animation("images/merge.gif", delay=2)
