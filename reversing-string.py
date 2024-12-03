# Programme to reverse a string | 27-11-24

user_input = input("Enter a word: ")

while True:
    try:
        Reversed = user_input[::-1]
        print(f"{user_input} -> {Reversed}")
        break
    except Exception as e:
        user_input = input(f"Provided input is not a string. [{user_input}]", "Error -> ", e)