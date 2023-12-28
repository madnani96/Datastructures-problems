#LeetCodeLink: https://leetcode.com/problems/invert-binary-tree/description/

def invertTree( root) :
        
        if root == None:
            return root
        else:
            root.left, root.right = root.right, root.left
            invertTree(root.left)
            invertTree(root.right)
        return root


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
invertTree(node2)