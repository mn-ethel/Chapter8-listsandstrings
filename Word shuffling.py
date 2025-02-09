from random import shuffle
sentence=input("Enter a sentence")
words=sentence.split()
shuffle(words)
final=' '.join(words)
print(f"{final}")
