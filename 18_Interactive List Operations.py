def display_menu():
    print("\nMenu:")
    print("1. Append")
    print("2. Insert")
    print("3. Pop")
    print("4. Remove")
    print("5. Quit")

numbers = [1, 2, 3, 4, 5]
print("Initial List:", numbers)

while True:
    display_menu()
    choice = input("Choose an option: ")

    if choice == '1':
        try:
            value = int(input("Enter value: "))
            numbers.append(value)
            print("Updated List:", numbers)
        except ValueError:
            print("Invalid input! Please enter an integer.")

    elif choice == '2':
        try:
            value = int(input("Enter value: "))
            index = int(input("Enter index: "))
            if 0 <= index <= len(numbers):
                numbers.insert(index, value)
                print("Updated List:", numbers)
            else:
                print("Index out of range!")
        except ValueError:
            print("Invalid input! Please enter integers.")

    elif choice == '3':
        try:
            index = int(input("Enter index to pop: "))
            if 0 <= index < len(numbers):
                popped_value = numbers.pop(index)
                print(f"Popped value: {popped_value}")
                print("Updated List:", numbers)
            else:
                print("Index out of range!")
        except ValueError:
            print("Invalid input! Please enter an integer.")

    elif choice == '4':
        try:
            value = int(input("Enter value to remove: "))
            if value in numbers:
                numbers.remove(value)
                print(f"Removed value: {value}")
                print("Updated List:", numbers)
            else:
                print(f"{value} not found in list!")
        except ValueError:
            print("Invalid input! Please enter an integer.")

    elif choice == '5':
        print("Exiting program.")
        break

    else:
        print("Invalid choice! Please choose a valid option.")
