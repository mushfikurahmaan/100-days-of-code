# Programme to check count the vowels in a given word | 26-11-24



user_input = input("Enter a word: ")

while True:
    # Check if the input is numeric
    if user_input.isdigit():
        user_input = input("Numbers are not words! Enter a valid word: ")
    else:
        break

# Define vowels
vowels = "aeiouAEIOU"

# Find unique vowels in the input word using a set
found_vowels = {char for char in user_input if char in vowels}

# Print the results
if len(found_vowels) != 0:
    print(f"In your given word: '{user_input}', there are {len(found_vowels)} unique vowels, and these are {sorted(found_vowels)}")
else:
    print(f"There are no vowels in your word: [{user_input}]")
