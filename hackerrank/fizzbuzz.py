def fizzbuzz():
    max_number = int_checker("Input an integer you want to perform FizzBuzz on:\n")
    for number in range(1, max_number + 1):
        if (number/3).is_integer():
            if (number/5).is_integer():
                print("FizzBuzz")
            else:
                print("Fizz")
        elif (number/5).is_integer():
            print("Buzz")
        else:
            print(number)

def int_checker(user_question):
    while True:
        try:
            return_value = int(input(user_question))
            break
        except Exception:
            print("That isn't an integer. Try again!")
    return return_value

fizzbuzz()