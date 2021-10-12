from visualiser.visualiser import Visualiser as vs


@vs(node_properties_kwargs={'shape': 'record', 'color': '#105585', 'style': 'filled', 'fillcolor': 'grey'})
def kth_grammer(k, n, op):

    if n < 1 or k < 1:
        return None

    if n == k == 1:
        return '0'

    op += kth_grammer(k, n-1, op)

    return "".join("01" if i == '0' else "10" for i in list(op))[k]


print(kth_grammer(1, 4, ''))
vs.make_animation('images/kth_grammer.png', delay=2)
