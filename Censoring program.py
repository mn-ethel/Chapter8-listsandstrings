import re

text = input("Enter some text: ")
curse_words = ["darn", "dang", "freakin", "heck", "shoot"]

censored_text = text

for curse in curse_words:
    censored_word = "*" * len(curse)  # Create the censored version
    # Use word boundaries (\b) to avoid censoring parts of other words
    censored_text = re.sub(r"\b" + curse + r"\b", censored_word, censored_text, flags=re.IGNORECASE)

print(censored_text)