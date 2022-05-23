from binarytree.structures import TreeNode


def make_tree_by(lst, idx):
    parent = None
    if idx < len(lst):
        value = lst[idx]
        if value == None:
            return

        parent = TreeNode(value)
        parent.left = make_tree_by(lst, 2 * idx + 1)
        parent.left = make_tree_by(lst, 2 * idx + 2)

    return parent