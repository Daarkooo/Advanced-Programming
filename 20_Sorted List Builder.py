user_list = []

while True:
    try:
        number = int(input("Enter a number: "))
        
        if number == 0:
            break
        
        user_list.append(number)
        
        print(f"Current List: {user_list}")
        print(f"Sorted List: {sorted(user_list)}")
        
    except ValueError:
        print("Please enter a valid integer.")

