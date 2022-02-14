# 104. Maximum Depth of Binary Tree (leetcode)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return(0)
        
        l=[]
        queue=[[root]]
        while queue:
            r=queue.pop(0)
            m=[]
            for i in r:
                m.append(i.val)
            l.append(m)
            
            j=[]
            for i in r:
                if(i.left!=None):
                    j.append(i.left)
                if(i.right!=None):
                    j.append(i.right)
            if j:
                queue.append(j)
        return(len(l))