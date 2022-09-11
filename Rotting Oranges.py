#SC -O(n)
#TC -O(n)
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        freshCount = 0
        time = -1
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append([i,j])
                elif grid[i][j] == 1:
                    freshCount+=1
        
        if freshCount == 0:
            return 0
        
        while q:
            size =len(q)
            time += 1
            while size:
                x,y = q.popleft()
                for dx,dy in dirs:
                    nr = x+dx
                    nc = y+dy
                    if 0<=nr and rows>nr and 0<=nc and cols>nc:
                        if grid[nr][nc] == 1:
                            q.append([nr,nc])
                            grid[nr][nc] = 2
                            freshCount-= 1
                size-=1
                        
        return time if freshCount == 0 else -1