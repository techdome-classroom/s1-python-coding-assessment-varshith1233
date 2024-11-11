class Solution:
    
    def countIslands(self, map: list[list[str]]) -> int:
        if not map or len(map) == 0:
            return 0

        num_islands = 0

        def markVisited(x: int, y: int):
            if x < 0 or y < 0 or x >= len(map) or y >= len(map[0]) or map[x][y] == 'W':
                return
            
            map[x][y] = 'W'

            markVisited(x + 1, y)
            markVisited(x - 1, y)
            markVisited(x, y + 1)
            markVisited(x, y - 1)

        for i in range(len(map)):
            for j in range(len(map[0])):
                if map[i][j] == 'L':
                    num_islands += 1
                    markVisited(i, j)

        return num_islands

