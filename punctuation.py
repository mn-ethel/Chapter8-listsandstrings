from random import shuffle
sentence=input("Enter a sentence:")
has_period=sentence.endswith('.')
if has_period:
    sentence=sentence[:-1]
words=sentence.split()
shuffle(words)
first_word=words[0]
Remaining_words=words[1:]

shuffled_sentence=[first_word.capitalize()]+Remaining_words
shuffled_sentence = ' '.join(shuffled_sentence) + ('.' if has_period else '')
print(shuffled_sentence)