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
def maxDepth(root) :
        
        if (root == None):
            return 0
        
        return 1+ max(maxDepth(root.left), maxDepth(root.right))
        
        if root == None:
            return 0
        level = 0
        q = deque([root]) 
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level

'''






node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node2.left = node3
node2.right = node4
node3.left = node5
node3.right = node6
#print(maxDepth(node2))

'''
Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2
'''

            
def isSameTree(p, q) -> bool:
        if p == None and q == None:
                return True 
            
        elif (p == None and q != None) or ( p != None and q == None) :
                return False
            
        elif p.val != q.val:
                return False
        else:
                return isSameTree(p.right, q.right) and isSameTree(p.left, q.left)


print(isSameTree(node2,node2))