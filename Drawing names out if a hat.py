import random

# Get the list of names from the user
names_input = input("Enter the names of the participants, separated by commas: ")
names = [name.strip() for name in names_input.split(",")]

# Get the number of entries for each participant
entries_input = input("Enter the number of entries for each participant, separated by commas: ")
entries = [int(entry.strip()) for entry in entries_input.split(",")]

# Create a list of participants where each name appears based on their number of entries
hat = []
for i in range(len(names)):
    hat.extend([names[i]] * entries[i])

# Randomly draw a winner
winner = random.choice(hat)

# Print the winner
print(f"The winner is: {winner}")
 