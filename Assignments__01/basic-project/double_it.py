def main():
    # Ask the user to enter a number
    curr_value = int(input("Enter a number: "))
    
    # Double the value until it reaches or exceeds 100
    while curr_value < 100:
        curr_value *= 2
        print(curr_value, end=" ")
67
# Python file to call the main() function.
if __name__ == '__main__':
    main()