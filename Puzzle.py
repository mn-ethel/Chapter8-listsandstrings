given_numbers = [
    "01265", "12171", "23257", "34548", "45970",
    "56236", "67324", "78084", "89872", "99414"
]

target_number = ""
for i in range(5):  # Iterate through each digit position
    target_number += given_numbers[i][i]  # Take the i-th digit from the i-th number

print(target_number)  