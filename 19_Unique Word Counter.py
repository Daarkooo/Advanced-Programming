unique_words = set()

while True:
    word = input("Enter a word: ").strip()
    
    if word in unique_words:
        print(f"You typed in {len(unique_words)} unique words.")
        break
    else:
        unique_words.add(word)
