# Program to check if a number is even or odd | 22-11-24

def main(num: int) -> str:
    if num % 2 == 0:
        return(f"{num} is even.")
    else:
        return(f"{num} is odd.")
    
if __name__ == "__main__":

    while True:
        user_input = input("Provide your number to check if it's even or odd: ")
        try:
            number = int(user_input)
            print(main(number))
            break

        except:
            print(f"Enter a valid number. [{user_input}] is not a number.")