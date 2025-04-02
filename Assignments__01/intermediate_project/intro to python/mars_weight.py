import random

NUM_ROUNDS: int = 5
MIN_VALUE: int = 1
MAX_VALUE: int = 100

def calculate_weight(earth_weight: float, planet: str) -> float:
    GRAVITY_MULTIPLIERS = {
        "Mercury": 0.376,
        "Venus": 0.889,
        "Mars": 0.378,
        "Jupiter": 2.36,
        "Saturn": 1.081,
        "Uranus": 0.815,
        "Neptune": 1.14
    }
    return round(earth_weight * GRAVITY_MULTIPLIERS.get(planet, 1.0), 2)

def main():
    print("Welcome to the High-Low Game!")
    print("--------------------------------")
    score = 0
    
    for round_num in range(1, NUM_ROUNDS + 1):
        print(f"Round {round_num}")
        player_number = random.randint(MIN_VALUE, MAX_VALUE)
        computer_number = random.randint(MIN_VALUE, MAX_VALUE)
        
        print(f"Your number is {player_number}")
        
        while True:
            guess = input("Do you think your number is higher or lower than the computer's? (higher/lower): ").strip().lower()
            if guess in ["higher", "lower"]:
                break
            print("Invalid input! Please enter either 'higher' or 'lower'.")
        
        if (guess == "higher" and player_number > computer_number) or (guess == "lower" and player_number < computer_number):
            print("You were right!")
            score += 1
        else:
            print("Aww, that's incorrect.")
        
        print(f"The computer's number was {computer_number}")
        print(f"Your score is now {score}\n")
    
    print("Thanks for playing!")
    if score == NUM_ROUNDS:
        print("Wow! You played perfectly!")
    elif score >= NUM_ROUNDS // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")
    
    # New Feature: Planetary Weight Calculation
    earth_weight = float(input("\nEnter a weight on Earth: "))
    planet = input("Enter a planet: ")
    planetary_weight = calculate_weight(earth_weight, planet)
    print(f"The equivalent weight on {planet}: {planetary_weight}")

if __name__ == '__main__':
    main()
