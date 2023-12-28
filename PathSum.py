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

'''
node2 = TreeNode(5)
node3 = TreeNode(4)
node4 = TreeNode(8)
node5 = TreeNode(11)
node6 = TreeNode(13)
node1 = TreeNode(4)
node7 = TreeNode(7)
node8 = TreeNode(2)
node2.right = node4
node2.left = node3
node3.left = node5
node4.left = node6
node4.right = node1
node5.left = node7
node5.right=node8
'''

'''
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 =TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node1.left = node2
node2.left = node3
node3.left = node4
node4.left =node5
'''
node1 = TreeNode(0)
node2 = TreeNode(2)
node3 =TreeNode(8)
node4 =TreeNode(-2)
node1.left = node2
node1.right=node3
node2.left = node4
def hasPathSum(root, targetSum) -> bool:
        
        def sum(root, target,targetSum):
            if root == None:
                return False
            elif (target+root.val) == targetSum:
                return True
            else:
                return sum(root.left,(target + root.val),targetSum) or sum(root.right,target+root.val,targetSum)
                
        return sum(root, 0, targetSum)
#print(hasPathSum(node2,22))
print(hasPathSum(node1,6))




