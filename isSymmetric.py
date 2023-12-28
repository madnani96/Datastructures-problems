#https://leetcode.com/problems/symmetric-tree/

from collections import deque


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


#  Our example tree looks like this:
#         2
#       /   \
#      3     4
#     / \
#    5   6


node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node2.left = node3
node2.right = node4
node3.left = node5
node3.right = node6

def isSymmetric(root) -> bool:
            
        def dfs (root1, root2):
                if not root1 and not root2:
                    return True
                if root1 == None or root2 == None:
                    return False
                return  (root1.val == root2.val) and dfs(root1.left, root2.right) and dfs(root1.right, root2.left)
        return dfs(root.left, root.right)
print(isSymmetric(node2))