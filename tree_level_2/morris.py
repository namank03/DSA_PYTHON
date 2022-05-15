# House robber in a binary tree
# with robbery -> root.data + l.no_rob + r.no_rob
# without robbery ->  max(l.rob, l.no_rob) + max(r.rob, r.no_rob)

def hourseRobberBt(root):
    if root is None: return 0

    l = hourseRobberBt(root.left)
    r = hourseRobberBt(root.right)

    rob, no_rob = 0, 0


