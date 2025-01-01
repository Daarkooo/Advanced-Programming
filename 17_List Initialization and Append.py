numbers = []
shoe_sizes = []

for num in [1, 2, 3, 4, 5]:
    numbers.append(num)

for size in [8, 9, 10, 11, 12]:
    shoe_sizes.append(size)

print("Numbers List:", numbers)
print("Shoe Sizes List:", shoe_sizes)

numbers.append(3)
numbers.append(5)
print("Updated Numbers List (with duplicates):", numbers)

combined_list = numbers + shoe_sizes
print("Combined List:", combined_list)
