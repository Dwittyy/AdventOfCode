puzzle_input = open("Day 11/puzzleinput.txt").read().splitlines()

def CountAdjacent(grid,row,col): # Counts the number of occupied seats adjacent to a position.
    width = len(grid[0]) - 1
    height = len(grid) - 1
    count = 0
    directions = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]
    for delti,deltj in directions:
        count += 0 <= row + delti <= height and 0 <= col + deltj <= width and grid[row+delti][col+deltj] == "#"
    return count

def CountVisible(grid,row,col): # Counts the number of occupied seats that are directly in line in each direction from a position.
    width = len(grid[0]) - 1
    height = len(grid) - 1
    count = 0
    directions = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]
    for delti,deltj in directions:
        row2 = row + delti
        col2 = col + deltj
        while (0 <= row2 <= height) and (0 <= col2 <= width):
            count += grid[row2][col2] == "#"
            if grid[row2][col2] != ".": break
            row2 += delti
            col2 += deltj
    return count

def UpdateSeats(grid,countfunction,val): # Goes through the grid and creates a new grid based on the flipping rules.
    changed = False
    newgrid = ["" for x in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "L" and countfunction(grid,i,j) == 0:
                newgrid[i] += "#"
                changed = True
            elif grid[i][j] == "#" and countfunction(grid,i,j) >= val:
                newgrid[i] += "L"
                changed = True
            else:
                newgrid[i] += grid[i][j]
    return newgrid,changed

grid = puzzle_input

while True:
    grid,changed = UpdateSeats(grid,CountVisible,5)
    if not changed: break

occupied = sum(row.count("#") for row in grid)

print(occupied)


