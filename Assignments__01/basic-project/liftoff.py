def main():
    # Countdown from 10 to 1 with a more dynamic approach
    countdown_start = 10
    for i in range(countdown_start, 0, -1):
        print(i, end=" ")
    
    # Print Liftoff! at the end
    print("🚀 Liftoff! 🚀")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()