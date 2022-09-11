# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#Approach 1
#SC -O(n)
#TC -O(n)
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        q = deque()
        q.append(root)
        
        while q and root:
            size = len(q)
            temp = []
            while size:
                node = q.popleft()
                if node:
                    temp.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
                else:
                    temp.append(None)
                size-=1
            if self.checkPalindrome(temp):
                continue
            else:
                return False
        
        return True
    
    def checkPalindrome(self,li):
        return li==li[::-1]
#=================================================
#Approach 2
#SC -O(n)
#TC -O(n)
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        q = deque()
        q.append(root.left)
        q.append(root.right)
        
        while q:
            """temp = []
            for v in q:
                if v:
                    temp.append(v.val)
                else:
                    temp.append(None)
            print(temp)"""
            left = q.popleft()
            right = q.popleft()
            if left == None and right == None:
                continue
            if left == None or right == None or left.val != right.val:
                return False
            
            q.append(left.left)
            q.append(right.right)
            q.append(left.right)
            q.append(right.left)
            
        return True
#=================================================
#Approach 3
#SC -O(n)
#TC -O(n)
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.dfs(root.left,root.right)  
        
    def dfs(self,left,right):
        if left == None and right == None:
            return True
        if left == None or right == None or left.val != right.val:
            return False
        return self.dfs(left.left,right.right) and self.dfs(left.right,right.left)