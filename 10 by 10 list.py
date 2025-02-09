import random

# Create the 10x10 list of random integers
my_list = [[random.randint(1, 100) for _ in range(10)] for _ in range(10)]


print("10x10 List:")
for row in my_list:
    print(row)

largest_in_third_row = max(my_list[2])
print("\nLargest value in the third row:", largest_in_third_row)
smallest_in_sixth_col = min(my_list[row][5] for row in range(10))  
print("\nSmallest value in the sixth column:", smallest_in_sixth_col)