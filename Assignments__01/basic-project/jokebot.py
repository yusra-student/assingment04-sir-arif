
PROMPT = "What do you want? "
JOKE = ("Here is a joke for you! Why do programmers prefer dark mode? "
        "Because light attracts bugs!")
SORRY = "Sorry, I only tell jokes."

# Get user input
user_input = input(PROMPT)

# Check the response
if user_input == "Joke":
    print(JOKE)
else:
    print(SORRY)
