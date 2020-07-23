# A full binary tree is a binary tree where each node has exactly 0 or 2 children. Return a list of all possible full
# binary trees with N nodes.  Each element of the answer is the root node of one possible tree. Each node of each
# tree in the answer must have node.val = 0.
# You may return the final list of trees in any order.


def allPossibleFBT(self, N):
    lst = []
    if N % 2 == 0:
        return []
    if N == 1:
        return [TreeNode(0)]

    for i in range(1, N, 2):

        for j in self.allPossibleFBT(i):

            for k in self.allPossibleFBT((N - i) - 1):
                rt = TreeNode(0)

                rt.left = j
                rt.right = k

                lst.append(rt)
    return lst
