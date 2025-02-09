import random

num_simulations = 1000
total_draws = 0

for _ in range(num_simulations):
    user_numbers = random.sample(range(1, 11), 6)  # User's 6 unique numbers
    draw_count = 0
    while True:
        draw_count += 1
        drawn_numbers = random.sample(range(1, 11), 6)  # Lottery drawing
        if set(user_numbers) == set(drawn_numbers):  # Check if sets are equal
            break  # User's numbers were drawn
    total_draws += draw_count

average_draws = total_draws / num_simulations
print(f"Average number of drawings: {average_draws}")