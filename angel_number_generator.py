import random

def main():
    print_disclaimer()
    How_many = ask_how_many()
    numbers = generate_numbers(How_many)
    print_numbers(numbers)


# This is to check the input to see if it was a number 1 -10 and not a letter.
def ask_how_many():
    while True:
        try:
            while True:
                how_many = int(input("How many numbers would you like from 1 - 10: "))
                if how_many > 0 and how_many <= 10:
                    return how_many
                else:
                    print("\nError Code 44: Input was not 1 - 10\n")
        except ValueError:
            print("\nError Code 55: Input was a letter\n")


def generate_numbers(How_many):
    numbers =  ["0",1,2,3,4,5,6,7,8,9,"10"]
    random_numbers = []

    for _ in range(How_many):
        random_numbers.append(random.choice(numbers))

    unique_numbers = remove_duplciates(random_numbers)
    return unique_numbers


def remove_duplciates(random_numbers):
    numbers = set()
    duplicates = set()
    unique_numbers = []

    # This checks for duplicates.
    for x in random_numbers:
        if x in numbers:
            duplicates.add(x)
        else:
            numbers.add(x)

    # This fixes the amount of numbers generated to match amount picked by the user.
    while len(numbers) < len(random_numbers):
        numbers.add(random.randrange(0, 10))

    # This changes the set to a list.
    for x in numbers:
        unique_numbers.append(x)

    random.shuffle(unique_numbers)
    return unique_numbers


def print_numbers(unique_numbers):
    print("\nAngel Numbers: ", end="")
    for numbers in unique_numbers:
        chance_of_change = random.randrange(0, 75)
        if numbers == "10":
            print(f"{numbers * random.randrange(1, 2)} ", end="")
        elif numbers == "0":
            print(f"{numbers * random.randrange(2, 4)} ", end="")
        else:
            if chance_of_change >= 70:   # 5% chance
                print(f"{numbers * 1111} ", end="")
            elif chance_of_change >= 50: # 25% chance
                print(f"{numbers * 111} ", end="")
            elif chance_of_change >= 25: # 25% chance
                print(f"{numbers * 11} ", end="")
            else:                        # 25% chance
                print(f"{numbers} ", end="")
    print("\n")

def print_disclaimer():
    print("--Version: 1.0--\nDISCLAIMER: This can be interperated as a source of angel numbers however since random take with a grain of salt.")

# This executes the main function.
main()