base_field = open("Day 3/puzzleinput.txt").read().splitlines()

def extendfield(current_field):
    for row in range(len(current_field)):
        current_field[row] = current_field[row] + base_field[row]
    return current_field



def counttrees(right,down):
    current_field = base_field.copy()

    trees = 0
    r = 0
    c = 0

    while r < len(current_field):
        if c >= len(current_field[r]):
            current_field = extendfield(current_field)
        trees += (current_field[r][c] == "#")
        r += down
        c += right

    return trees

product = counttrees(1,1) * counttrees(3,1) * counttrees(5,1) * counttrees(7,1) * counttrees(1,2)

print(product)