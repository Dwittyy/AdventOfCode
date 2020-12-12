puzzle_input = open("Day 11/puzzleinput.txt").read().splitlines()

def CountAdjacent(grid,row,col,char):
    width = len(grid[0]) - 1
    height = len(grid) - 1
    count = 0
    if row > 0:
        count += (grid[row-1][col] == char)
    if row < height:
        count += (grid[row+1][col] == char)
    if col > 0:
        count += (grid[row][col-1] == char)
    if col < width:
        count += (grid[row][col+1] == char)
    if row > 0 and col > 0:
        count += (grid[row-1][col-1] == char)
    if row > 0 and col < width:
        count += (grid[row-1][col+1] == char)
    if row < height and col > 0:
        count += (grid[row+1][col-1] == char)
    if row < height and col < width:
        count += (grid[row+1][col+1] == char)
    return count

def UpdateSeats(grid):
    changes = 0
    newgrid = ["" for x in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "L" and CountAdjacent(grid,i,j,"#") == 0:
                newgrid[i] += "#"
                changes += 1
            elif grid[i][j] == "#" and CountAdjacent(grid,i,j,"#") >= 4:
                newgrid[i] += "L"
                changes += 1
            else:
                newgrid[i] += grid[i][j]
    if changes == 0:
        print("no changes!")
        return False
    return newgrid

grid = puzzle_input

while UpdateSeats(grid):
    grid = UpdateSeats(grid)

occupied = 0
for row in grid:
    occupied += row.count("#")

print(grid[0])
print(occupied)


