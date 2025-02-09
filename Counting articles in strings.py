S=input("Enter some text")
articles=['a','an','the']
words=S.lower().split()
count=0
for word in words:
    if word in articles:
        count=count+1
    else:
        count=count
print(f"The number of articles in the word is {count}")
