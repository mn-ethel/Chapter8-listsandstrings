import random
size=6
characters=['@', '5', '#', 'A', '!', '0', 'b', '$', 'N', 'x', '-', '+', 'c', ':'] * 2  # Two of each
random.shuffle(characters)
matrix = []
for i in range(size):
    row = []
    for j in range(size):
       row.append(characters[i * size + j]) # Append characters to the row.
    matrix.append(row)

# Print the matrix
for row in matrix:
    print(' '.join(row)) # Print each row with spaces between characters.
