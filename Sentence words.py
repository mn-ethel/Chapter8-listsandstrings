sentence=input("Enter a sentence:")
words=sentence.split()
if len(words)>=3:
    third_word=words[2]
    print(f"The third word of the sentence is {third_word}")
else:
    print("The sentence has less than three words")

