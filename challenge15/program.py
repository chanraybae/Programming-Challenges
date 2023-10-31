# Name: Chanwoo Ray Bae
# Course: Coding Quandaries
# Coding Quandary 15

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def build_tree(data_iter):
    value = next(data_iter)
    if value == -1:
        return None
    node = Node(value)
    node.left = build_tree(data_iter)
    node.right = build_tree(data_iter)
    return node


def max_concurr(root):
    if not root:
        return None
    q = [(root, 1)]
    lvl_nodes = {}
    while q:
        node, lvl = q.pop(0)
        if lvl not in lvl_nodes:
            lvl_nodes[lvl] = 0
        lvl_nodes[lvl] += 1
        if node.left:
            q.append((node.left, lvl + 1))
        if node.right:
            q.append((node.right, lvl + 1))
    max_lvl, max_nodes = max(lvl_nodes.items(), key=lambda x: x[1])
    return max_lvl, max_nodes


def main():
    try:
        while True:
            workflow = list(map(int, input().strip().split()))
            if workflow:  # check if the workflow list is not empty
                root = build_tree(iter(workflow))
                max_lvl, max_nodes = max_concurr(root)
                print(f"Level {max_lvl} has the most nodes: {max_nodes}")
    except EOFError:
        pass


if __name__ == "__main__":
    main()
