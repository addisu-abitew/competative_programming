# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def isValid(cur_nodes):
            vals = []
            for node in cur_nodes:
                if node:
                    vals.append(node.val)
                else:
                    vals.append(node)
            return vals == vals[::-1]
        
        def nextNodes(cur_nodes):
            next_nodes = []
            for node in cur_nodes:
                if node:
                    next_nodes.append(node.left)
                    next_nodes.append(node.right)
            return next_nodes
        
        cur_nodes = [root]
        while len(cur_nodes) > 0:
            if isValid(cur_nodes):
                cur_nodes = nextNodes(cur_nodes)
            else:
                return False
        return True