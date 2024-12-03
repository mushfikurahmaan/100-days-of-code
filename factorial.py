# Programme to find factorial of a given number | 23-11-24


def req_factorial(number : int) -> int:
    if number == 1 or number == 0:
        return 1
    else:
        return number * req_factorial(number - 1)
    
if __name__ == "__main__":

    while True:
        try:
            user_input = input("Enter the number to get the factorial of it: ")
            IntNumber = int(user_input)
            if IntNumber < 0:
                print("Sorry, negative numbers doesn't have factorials.")
            else:
                factorial = req_factorial(IntNumber)
                print(f"{IntNumber}! = {factorial}")
                break
        except:
            print(f"Please provide a valid number. {user_input} is not a number")