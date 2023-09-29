# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        def calcAv(nodes):
            vals = [node.val for node in nodes]
            return float(sum(vals))/len(vals)
        
        def nextNodes(nodes):
            next_nodes = []
            for node in nodes:
                if node.left:
                    next_nodes.append(node.left)
                if node.right:
                    next_nodes.append(node.right)
            return next_nodes
        
        averages = []
        cur_nodes = [root]
        while len(cur_nodes) > 0:
            cur_av = calcAv(cur_nodes)
            averages.append(cur_av)
            cur_nodes = nextNodes(cur_nodes)
        return averages