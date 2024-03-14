import random

class Questions:
    def __init__(quiz, question, answer):
        quiz.question = question
        quiz.answer = answer


curr_user = input("Please enter your name: ")
print(f"Hello {curr_user}!")
print("""Welcome to the Film Quotes Quiz 2024\n
Please complete the film quote by adding the missing word - \n""")

corr_count = 0

q1 = Questions("\"Frankly my dear, I don't give a ___ \"", "damn")
q2 = Questions("\"We're going to need a bigger ___ \"", "boat")
q3 = Questions("\"You had me at ___ \"", "hello")
q4 = Questions("\"You can't handle the ___ \"","truth")
q5 = Questions("\"I'm going to make him an offer he can't ___\"", "refuse")
q6 = Questions("\"Hasta la vista, ___ \"", "baby")
q7 = Questions("\"Toto, I've a feeling we're not in ___ anymore\"", "kansas")
q8 = Questions("\"Here's looking at you, ___ \"", "kid")
q9 = Questions("\"Get your stinking paws off me, you damn dirty ___\"", "ape")
q10 = Questions("\"I see ___ people\"","dead")

full_quiz = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]

random.shuffle(full_quiz)
for q in full_quiz:
    print(q.question)
    answer = input("Finish the quote: ").lower()
    if answer == q.answer:
        print("Correct!\n") 
        corr_count += 1
        print("Next question:")
        continue
    else:
        print("Incorrect!\n")
        print("Next question: ")
        continue

print("")
print(f"""Congratulations {curr_user}, you've reached the end of the Film Quote Quiz!
      You answered {corr_count} questions correctly from a total of {len(full_quiz)} questions\n""")
