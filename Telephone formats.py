phone_number=input("Enter phone number:")
if phone_number.isdigit() and len(phone_number)==12 and phone_number[3]=='-'and phone_number[7]=='-'and phone_number[0]!='0':
    print("Valid")
elif phone_number[0]=='1' and phone_number[1:].isdigit() and len(phone_number)==13 and phone_number[4]=='-' and phone_number[8]=='-':
    print("Valid")
else:
    print("Invalid")
