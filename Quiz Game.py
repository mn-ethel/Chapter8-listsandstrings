import random
Questions=['What is the smallest prime number?','How many continents are there?','What is the chemical symbol for gold?',
           'In what year did world War II begin?','What is the capital of France?','How many teeth does an adult human typically have?',
           'What is the largest planet in the solar system?','Who painted the Mona Lisa?','What is the name of the largest ocean on earth?','How many bones are in the average adult human body?']
Answers=['2','7','Au','1939','Paris','32','Jupiter','Leonardo da Vinci','The Pacific Ocean','206']
score=0
num_questions=4
question_indices = random.sample(range(len(Questions)), num_questions)
for i in range(num_questions):
    question_index=question_indices[i]
    question=Questions[question_index]
    correct_answer=Answers[question_index]
    user_answer=input(f"Question{i+1}:{question}")
    if user_answer.lower() == correct_answer.lower():  # Case-insensitive comparison
        print("Correct!")
        score += 1
    else:
        print(f"Incorrect. The answer is {correct_answer}.")
        score=score

print(f"You got {score} out of {num_questions} correct.")

