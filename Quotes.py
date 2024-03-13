
counter = 0
question = 0

curr_user = input("What's your name?: ")
print(f"Hello {curr_user}!")
print("""\nWelcome to the Film Quotes Quiz 2024\n
Please complete the film quote by adding the missing word- \n""")
print("")

print("Quote ONE - \"Frankly my dear, I don't give a ...\"")
answer = input("Complete the quote - ")
print(f"You answered {answer}")
if str(answer).lower() == "damn":
    counter += 1
    question += 1
    print("Correct!")
else: 
    print("Incorrect!")
    question += 1

print("")
print("Quote TWO - \"We're going to need a bigger ...\"")
answer = input("Complete the quote - ")
print(f"You answered {answer}")
if str(answer).lower() == "boat":
    counter += 1
    question += 1
    print("Correct!")
else:
    print("Incorrect!")
    question += 1

print("")
print("Quote THREE - \"You had me at ...\"")
answer = input("Complete the quote - ")
print(f"You answered {answer}")
if str(answer).lower() == "hello":
    counter += 1
    question += 1
    print("Correct!")
else:
    print("Incorrect!")
    question += 1

print("")
print("Quote FOUR - \"We're going to need a bigger ...\"")
answer = input("Complete the quote - ")
print(f"You answered {answer}")
if str(answer).lower() == "boat":
    counter += 1
    question += 1
    print("Correct!")
else:
    print("Incorrect!")
    question += 1

print("")
print("Quote FIVE - \"You can't handle the ...\"")
answer = input("Complete the quote - ")
print(f"You answered {answer}")
if str(answer).lower() == "truth":
    counter += 1
    question += 1
    print("Correct!")
else:
    print("Incorrect!")
    question += 1

print("")
print("Quote SIX - \"I'm going to make him an offer he can't ...\"")
answer = input("Complete the quote - ")
print(f"You answered {answer}")
if str(answer).lower() == "refuse":
    counter += 1
    question += 1
    print("Correct!")
else:
    print("Incorrect!")
    question += 1

print("")
print("Quote SEVEN - \"Get your stinking paws off me, you damn dirty ...\"")
answer = input("Complete the quote - ")
print(f"You answered {answer}")
if str(answer).lower() == "ape":
    counter += 1
    question += 1
    print("Correct!")
else:
    print("Incorrect!")
    question += 1

print("")
print("Quote EIGHT - \"Toto, I've a feeling we're not in ... anymore\"")
answer = input("Complete the quote - ")
print(f"You answered {answer}")
if str(answer).lower() == "kansas":
    counter += 1
    question += 1
    print("Correct!")
else:
    print("Incorrect!")
    question += 1

print("")
print("Quote NINE - \"Here's looking at you, ...\"")
answer = input("Complete the quote - ")
print(f"You answered {answer}")
if str(answer).lower() == "kid":
    counter += 1
    question += 1
    print("Correct!")
else:
    print("Incorrect!")
    question += 1

print("")
print("Quote TEN - \"Hasta la vista, ...\"")
answer = input("Complete the quote - ")
print(f"You answered {answer}")
if str(answer).lower() == "baby":
    counter += 1
    question += 1
    print("Correct!")
else:
    print("Incorrect!")
    question += 1

print(f"""Congratulations {curr_user}, you've reached the end of the Quote Quiz!
      You answered {counter} questions correctly from a total of {question} questions""")





