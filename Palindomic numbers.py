palindromic_numbers=[]
for i in range (100,1001):
   number=str(i)# convert to string
   if number==number[::-1]:
     palindromic_numbers.append(i)
print(palindromic_numbers)

