num_list=[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [1,14,15,16]
]
total_sum=0
num_elements=0
for row in num_list:
    for element in row:
        total_sum+=element
        num_elements+=1
average=total_sum/num_elements
print(f"The average is:{average}")
