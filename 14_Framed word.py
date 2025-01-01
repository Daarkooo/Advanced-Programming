word = input("Word: ")

frame_width = 30
padding = (frame_width - len(word)) // 2

# Print the top and bottom border of the frame
print("*" * frame_width)

# Print the word in the center
print(" " * padding + word + " " * (frame_width - len(word) - padding))

# Print the right border of the frame
print("*" * frame_width)
