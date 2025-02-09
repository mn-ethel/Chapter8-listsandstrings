
square = [
    [16, 2, 3, 13],
    [5, 11, 10, 8],
    [9, 7, 6, 12],
    [4, 14, 15, 1]
]

size = 4  # Since it's a 4×4 square
magic_sum = sum(square[0])  # Reference sum (sum of the first row)

# Check rows
is_magic = True
for row in square:
    if sum(row) != magic_sum:
        is_magic = False

# Check columns
for col in range(size):
    if sum(square[row][col] for row in range(size)) != magic_sum:
        is_magic = False

# Check main diagonal
if sum(square[i][i] for i in range(size)) != magic_sum:
    is_magic = False

# Check secondary diagonal
if sum(square[i][size - 1 - i] for i in range(size)) != magic_sum:
    is_magic = False

# Print result
if is_magic:
    print("It is a magic square!")
else:
    print("It is NOT a magic square.")
