import random

def computer_guess():
    low, high = 1, 100
    attempts = 0
    feedback = ""
    
    print("Think of a number between 1 and 100. I will try to guess it!")
    
    while feedback != "correct":
        guess = random.randint(low, high)
        attempts += 1
        
        feedback = input(f"Is {guess} too high, too low, or correct? ").lower()
        
        if feedback == "too high":
            high = guess - 1
        elif feedback == "too low":
            low = guess + 1
        elif feedback == "correct":
            print(f"Yay! I guessed your number in {attempts} attempts! 🎉")
        else:
            print("Please enter a valid response: 'too high', 'too low', or 'correct'.")

if __name__ == "__main__":
    computer_guess()