from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numIslandsFound = 0
        """
        1. Translate the problem into graph terminology
        vertex - is a cell
        edge - neibhboring cells
        no paths or weights

        2. build your graph 
        problem set has graph in a 2d array

        3. traverse the graph/grid
        if we find a 1:
            incremend numIslandswe 
            then want to traverse all of its connected components
        and mark them as vistied
        return numIslands
        """
        # input validation
        if len(grid) == 0: 
            return 0

        width, height = len(grid[0], len(grid))
        # initializing a 2d grid [false, false, ..
        #                         false, ...true      ]
        # visited[i][j] is True if cell in grid[i][j] has been visted
        visited = [[False] * width for x in range(height)]
        for y in range(height):
            for x in range(width):
                # is the element land/"1"
                if grid[y][x] == '1' and not visited[y][x]:
                    self.numIslandsFound += 1
                    self.markConnectedComponentsAsVisited(grid, visited, x, y)
        return self.numIslandsFound

    # start at x, y and mark connected components that are 1 visited
    def markConnectedComponentsAsVisited(self, grid, visited, x, y):
        width, height = len(grid[0]), len(grid)
        stack = deque()
        stack.append((x, y))
        while len(stack) > 0:
            x, y = stack.pop()
            if visited[y][x]:
                continue
            visited[y][x] = True
            # Traverse all adjacent nodes that are also 1
            # check left node
            if x - 1 >= 0 and grid[y][x - 1] == '1':
                stack.append((x - 1, y)) 
            # check right node
            if x - 1 < width and grid[y][x + 1] == '1':
                stack.append((x + 1, y))
            # check top node
            if y - 1 >= 0 and grid[y - 1][x] == '1':
                stack.append((x, y - 1))
            #check bottom node
            if y - 1 < height and grid[y + 1][x] == '1':
                stack.append((x, y + 1))
            