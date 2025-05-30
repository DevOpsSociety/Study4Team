from pprint import pprint
import copy
import random
import sys

sys.setrecursionlimit(2000)

def find_next_empty(puzzle):
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c
    
    return None, None

def is_valid(puzzle, guess, row, col):
    if guess in puzzle[row]:
        return False
    if guess in [puzzle[r][col] for r in range(9)]:
        return False
    
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False
    
    return True


def solve_sudoku(puzzle):
    row, col = find_next_empty(puzzle)
    if row is None:
        return True
    
    numbers = list(range(1,10))
    random.shuffle(numbers)
    
    for guess in numbers:
        if is_valid(puzzle, guess, row, col):
            puzzle[row][col]= guess
            if solve_sudoku(puzzle):
                return True
        
            puzzle[row][col] = -1
    
    return False

def generate_full_board():
    board = [[-1 for _ in range(9)] for _ in range(9)]
    solve_sudoku(board)
    return board

def make_puzzle(board, empty_cells=40):
    puzzle = copy.deepcopy(board)
    cells = [(r, c) for r in range(9) for c in range(9)]
    random.shuffle(cells)

    count = 0
    for r, c in cells:
        if count >= empty_cells:
            break
        puzzle[r][c] = -1
        count += 1
    return puzzle

if __name__ == "__main__":
    full_board = generate_full_board()
    puzzle = make_puzzle(full_board, empty_cells=40)

    print("스도쿠 퍼즐:")
    pprint(puzzle)

    input("\n 엔터를 누르면 정답을 보여줍니다.")

    print("\n 정답:")
    pprint(full_board)



