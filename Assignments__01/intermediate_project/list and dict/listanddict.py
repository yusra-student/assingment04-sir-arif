def create_fruit_list():
    fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']
    print(f"Initial list: {fruit_list}")
    print(f"List length: {len(fruit_list)}")
    
    fruit_list.append('mango')
    print(f"Updated list: {fruit_list}")

def access_element(lst, index):
    if 0 <= index < len(lst):
        return lst[index]
    return "Index out of range!"

def modify_element(lst, index, new_value):
    if 0 <= index < len(lst):
        lst[index] = new_value
        return f"Updated list: {lst}"
    return "Index out of range!"

def slice_list(lst, start, end):
    if 0 <= start < len(lst) and 0 <= end <= len(lst) and start < end:
        return lst[start:end]
    return "Invalid index range!"

def list_game():
    my_list = ['apple', 'banana', 'cherry', 'date', 'fig']
    
    while True:
        print("\nChoose an operation:")
        print("1. Access an element")
        print("2. Modify an element")
        print("3. Slice the list")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            index = int(input("Enter an index: "))
            print(access_element(my_list, index))
        elif choice == '2':
            index = int(input("Enter an index: "))
            new_value = input("Enter a new value: ")
            print(modify_element(my_list, index, new_value))
        elif choice == '3':
            start = int(input("Enter start index: "))
            end = int(input("Enter end index: "))
            print(f"Sliced list: {slice_list(my_list, start, end)}")
        elif choice == '4':
            print("Exiting game!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 4.")

if __name__ == "__main__":
    create_fruit_list()
    list_game()
