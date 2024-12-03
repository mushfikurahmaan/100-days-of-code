def main():
    while True:
        user_input = input("Enter a number: ")
        if user_input.isdigit():
            print(prime(int(user_input)))
            break
        else:
            print(f"[{user_input}] is not a number.")



def prime(number):
    if number <= 1:
        return f"{number} is not a prime number. Must be POSTIVE INTEGER and greater then [0 & 1]"
    elif number == 2:
        return "2 is the smallest and the only even prime number."
    else:
        for i in range(2, int(number*0.5)+1):
            if number % i == 0:
                return f"{number} is not a prime number. It is divisible by {i}."

        else:
            return f"{number} is a prime number."

if __name__ == "__main__":
    main()