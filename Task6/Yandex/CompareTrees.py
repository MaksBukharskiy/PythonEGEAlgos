def SolutionOfCompareTrees(tree1: TreeNode | None, tree2: TreeNode | None) -> False:
    if (not tree1) or (not tree2):
        return True

    if not tree1 or not tree2:
        return False

    if tree1.val != tree2.val:
        return False

    ans = SolutionOfCompareTrees(tree1.left, tree2.left) and SolutionOfCompareTrees(tree1.right, tree2.right)

    return ans