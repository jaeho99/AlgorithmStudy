from collections import deque

from binarytree.structures import TreeNode


def make_tree_by(lst, idx):
    parent = None
    if idx < len(lst):           #
        value = lst[idx]
        if value is None:
            return

        parent = TreeNode(value)
        parent.left = make_tree_by(lst, 2 * idx + 1)
        parent.right = make_tree_by(lst, 2 * idx + 2)

    return parent


def make_lst_by(root):
    if not root:
        return []

    lst = []
    q = deque([root])

    while q:
        node = q.popleft()
        lst.append(node.val)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

    return lst
