import collections
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        visited=set()
        count=0
        q=collections.deque()
        rows,cols=len(board),len(board[0])
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=='X' and (r,c)not in visited:
                    count+=1
                    q.append((r,c))
                    visited.add((r,c))
                    while q:
                        row, col = q.popleft()
                        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                            nr, nc = row + dr, col + dc
                            if (0 <= nr < rows and 0 <= nc < cols and
                                board[nr][nc] == 'X' and (nr, nc) not in visited):
                                visited.add((nr, nc))
                                q.append((nr, nc))
        return count

        