# Name: Chanwoo Ray Bae
# Course: Coding Quandaries
# Coding Quandary 13

import sys
from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def construct_min_height_bst(sorted_arr, start_index, end_index):
    if start_index > end_index:
        return None
    mid_index = start_index + (end_index - start_index + 1) // 2
    node = TreeNode(sorted_arr[mid_index])
    node.left = construct_min_height_bst(sorted_arr, start_index, mid_index - 1)
    node.right = construct_min_height_bst(sorted_arr, mid_index + 1, end_index)
    return node


def print_nodes_in_lvl_order(root_node):
    if not root_node:
        return
    curr_lvl_nodes = deque([root_node])

    while curr_lvl_nodes:
        lvl_output = []
        next_lvl_nodes = deque([])

        while curr_lvl_nodes:
            node = curr_lvl_nodes.popleft()
            lvl_output.append(str(node.value))
            if node.left:
                next_lvl_nodes.append(node.left)
            if node.right:
                next_lvl_nodes.append(node.right)
        print(' '.join(lvl_output))
        curr_lvl_nodes = next_lvl_nodes


def main():
    test_cases = sys.stdin.read().strip().split('\n')
    for test_case in test_cases:
        input_arr = list(map(int, test_case.strip().split()))
        root_node = construct_min_height_bst(input_arr, 0, len(input_arr) - 1)
        print_nodes_in_lvl_order(root_node)


if __name__ == "__main__":
    main()
