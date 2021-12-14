import sys, os

sys.path.append(os.getcwd())
from util.read import read, read_nums

puzzle_input = read(2021, 4)

# Parse Draws
draws = [int(x) for x in puzzle_input.pop(0).split(",")]

# Parse Boards
boards = []
board = {}
row = 1
for line in puzzle_input[1:]:
    if line != "":
        line = [num for num in line.split(" ") if num != ""]
        for column, digit in enumerate(line):
            board[(row, column + 1)]= {"num": int(digit), "marked": False}
        row += 1
    else:
        boards.append(board)
        board = {}
        row = 1

def check_line(board,direction,number):
    check_tiles = [tile for tile in list(board.keys()) if tile[direction] == number]
    marks = [board[tile]["marked"] for tile in check_tiles]
    return (sum(marks) == 5)

def calculate_score(grid, draw):
    return sum([tile["num"] for tile in grid.values() if not tile["marked"]]) * draw

def play_bingo():
    for num in draws:
        for board in boards:
            for tile in list(board.keys()):
                if board[tile]["num"] == num:
                    board[tile]["marked"] = True
                    if check_line(board,0,tile[0]) or check_line(board,1,tile[1]):
                        score = calculate_score(board,num)
                        print(f"found line on number {num} with score {score}!")
                        print(board)
                        return

def play_reverse_bingo():
    winning_boards = []
    winning_draws = []
    for draw in draws:
        for board in boards:
            if board in winning_boards:
                continue
            for tile in list(board.keys()):
                if board[tile]["num"] == draw:
                    board[tile]["marked"] = True
                    if check_line(board,0,tile[0]) or check_line(board,1,tile[1]):
                        winning_boards.append(board)
                        winning_draws.append(draw)

    last_winning_board, last_winning_draw =  winning_boards[-1], winning_draws[-1]
    score = calculate_score(last_winning_board,last_winning_draw)
    print(f"the last picked board is on number {last_winning_draw} with score {score}!")
    #print(last_winning_board)




play_reverse_bingo()