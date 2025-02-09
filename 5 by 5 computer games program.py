import random

rows = 5
cols = 5

# Create the 5x5 list of zeros
matrix = [[0 for _ in range(cols)] for _ in range(rows)]

# Find coordinates of all zeros
zero_coordinates = []
for i in range(rows):
    for j in range(cols):
        if matrix[i][j] == 0:
            zero_coordinates.append([i, j])

if not zero_coordinates:  # Check if all entries are one (no zeros)
    print("All entries are one.")
else:
    # Pick a random zero and change it to one
    random_coordinate = random.choice(zero_coordinates)
    row, col = random_coordinate
    matrix[row][col] = 1

    # Print the updated matrix
    for row in matrix:
        print(row)