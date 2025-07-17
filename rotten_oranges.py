import collections
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        queue=collections.deque()
        fresh=0
        time=0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==2:
                    queue.append((i,j,0))
                elif grid[i][j]==1:
                    fresh+=1
        dir=[(-1,0),(1,0),(0,1),(0,-1)]
        while queue:
            r,c,t=queue.popleft() 
            for x,y in dir:
                nr,nc=r+x,c+y
                if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]==1:
                    grid[nr][nc]=2
                    fresh-=1
                    queue.append((nr,nc,t+1))
                    time=t+1
        return time if fresh==0 else -1





        



        