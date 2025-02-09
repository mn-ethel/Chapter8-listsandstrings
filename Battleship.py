
board = [
    [0, 1, 0, 0, 1],
    [1, 0, 0, 1, 0],
    [0, 0, 1, 0, 0],
    [0, 1, 0, 0, 1],
    [1, 0, 0, 1, 0]
]

# Get user input for row and column
row = int(input("Enter row (0-4): "))
col = int(input("Enter column (0-4): "))

if 0 <= row < 5 and 0 <= col < 5:
    if board[row][col] == 1:
        print("Hit!")
    else:
        print("Miss!")
else:
    print("Invalid input! Please enter numbers between 0 and 4.")
