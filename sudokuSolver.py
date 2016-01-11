#sudoku solver

#grid constants
grid_height = 9
grid_width = 9
subgrid_dimensions = 3

col = [i % grid_width for i in range(grid_height*grid_width)]
row = [i // grid_width for i in range(grid_height*grid_width)]
subgrid = [i // subgrid_dimensions%subgrid_dimensions + j * subgrid_dimensions
           for j in range(subgrid_dimensions) for i in range(grid_width*subgrid_dimensions)]

def parseGrid(g):
    return [int(ch) for ch in g]

def printGrid(grid):
    for i in range(grid_width):
        for j in range(grid_height):
            print(grid[i*grid_width+j], end="")
        print()

def solve(grid):
    if 0 not in grid:
        printGrid(grid)
    for i in range(grid_height*grid_width):
        if grid[i] == 0:
            ind = list(filter(lambda x: col[x] == col[i] or row[x] == row[i] or subgrid[x] == subgrid[i],
                              range(grid_height*grid_width)))
            notPossibles = set()
            for index in ind:
                notPossibles.add(grid[index])
            possibles = set(range(1, 1 + grid_width)).difference(notPossibles)
            for p in possibles:
                newGrid = list(grid)
                newGrid[i] = p
                solve(newGrid)
            return

grid = (parseGrid("000000000075200000680500049000080004901000305800020000750003061000008930000000000"))
solve(grid)
