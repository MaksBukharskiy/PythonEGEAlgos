def solutionTreeLength(tree: TreeNode | None) -> int:
    if not tree:
        return 0

    treeLeft = solutuionTreeLenght(tree.left)
    treeRight = solutuionTreeLenght(tree.rigth)

    ans =  max(treeLeft, treeRight) +1

    return ans