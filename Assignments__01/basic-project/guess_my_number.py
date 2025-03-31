import random

def main():
    # Generate a random number between 0 and 99
    secret_number = random.randint(0, 99)
    attempts = 0  # Track the number of attempts
    
    print("I am thinking of a number between 0 and 99...")
    
    while True:
        try:
            guess = int(input("Enter a guess: "))
            attempts += 1
            
            if guess < 0 or guess > 99:
                print("Please enter a number between 0 and 99.")
            elif guess < secret_number:
                print("Your guess is too low")
            elif guess > secret_number:
                print("Your guess is too high")
            else:
                print(f"Congrats! The number was: {secret_number}")
                print(f"You guessed it in {attempts} attempts!")
                break
        except ValueError:
            print("Invalid input! Please enter a number.")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
