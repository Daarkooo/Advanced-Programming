num = int(input("How many people need a ride? "))

v = int(input("How many people fit in one taxi? "))

num_taxis = num // v

if num % v != 0:
    num_taxis = num_taxis + 1
else:
    num_taxis = num_taxis

# Display the result
print(f"Number of taxis needed: {num_taxis}")
