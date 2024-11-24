# Programme to find out the largest number in a list | 24-11-24

numbers = [0,2,-8,4,5,-6,7]
largest_number = numbers[0]

def main(number):
    global largest_number
    for i in number:
        if i > largest_number:
            largest_number = i
    return largest_number


if __name__ == "__main__":
    main(numbers)
    print(largest_number)
    
    