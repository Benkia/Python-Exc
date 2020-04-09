class Node(object):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)


def get_goal(node, level=0):
    results = []
    if node.name == "Goal":
        return node.name
    for node_child in node.children:
        results.append(get_goal(node_child,
                                level + 1))
    for result in results:
        if result is not None:
            if level > 0:
                return ("{} -> {}".format(node.name,
                                          result))
            else:
                print("{} -> {}".format(node.name,
                                        result))
    return


a = Node('A')
a_goal = Node('Goal')
goal = Node('Goal')
b = Node('B')
c = Node('C')
d = Node('D')
e = Node('E')
f = Node('F')
g = Node('G')
h = Node('H')
i = Node('I')
j = Node('J')
k = Node('K')
l = Node('L')
m = Node('M')

a_goal.add_child(e)
a.add_child(a_goal)
a.add_child(b)
b.add_child(c)
b.add_child(goal)
a.add_child(d)
d.add_child(goal)
a.add_child(f)
a.add_child(g)
f.add_child(h)
f.add_child(i)
i.add_child(m)
i.add_child(j)
h.add_child(k)
h.add_child(l)
l.add_child(goal)

get_goal(a)
