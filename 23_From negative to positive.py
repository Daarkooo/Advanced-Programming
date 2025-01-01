while True:
    try:
        N = int(input("Please enter a positive integer: "))
        if N <= 0:
            print("Please enter a positive integer greater than zero.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

for i in range(-N, N + 1):
    if i != 0:
        print(i)
