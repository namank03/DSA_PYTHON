from visualiser.visualiser import Visualiser as vs


@vs(node_properties_kwargs={"shape": "record", "color": "#f57542", "style": "filled", "fillcolor": "grey"})
def all_inc_subsequence(arr, op):
    if len(arr) < 1:
        print(op)
        return

    for i in range(len(arr)):
        try:
            if op[-1] < arr[i]:
                all_inc_subsequence(arr[i + 1:], op + [arr[i]])
            else:
                all_inc_subsequence(arr[i + 1:], op)
        except Exception as e:
            all_inc_subsequence(arr[i + 1:], op + [arr[i]])


all_inc_subsequence([1, 2, 4, 3], [])
vs.make_animation('images/lis.gif', delay=2)
