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
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        q = deque()
        q.append(root)
        
        while q:
            size = len(q)
            level =[]
            for _ in range(size):
                node = q.popleft()
                level.append(node.val)
                if node.left and node.right and ((node.right.val == x and node.left.val == y) or (node.right.val == y and node.left.val == x)):
                    return False
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            if x in level and y in level:
                return True
        
        return False
#===================================================
#Approach 2
#SC -O(n)
#TC -O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        self.x = x
        self.y = y
        self.x_ht = 0
        self.y_ht = 0
        self.x_parent = None
        self.y_parent = None
        self.dfs(root,None,0)
        return self.x_ht == self.y_ht and self.x_parent!=self.y_parent
    
    def dfs(self,root,parent,level):
        if root == None:
            return
        if root.val == self.x:
            self.x_ht = level
            self.x_parent = parent
        
        if root.val == self.y:
            self.y_ht = level
            self.y_parent = parent
        
        self.dfs(root.left,root,level+1)
        self.dfs(root.right,root,level+1)