def max_depth(tree1: TreeNode | None) -> int:
    if not tree1:
        return 0

    left_depth = max_depth(tree1.left)
    right_depth = max_depth(tree1.right)

    ans = max(left_depth, right_depth) + 1

    return ans