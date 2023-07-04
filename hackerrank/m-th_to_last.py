def element_from_last():
    mth_to_last = int_checker("What element from the list from last do you want to pick?\n")

    list_of_elements = []
    list_finished = False
    while list_finished == False:
        element = input("Type the elements you want in your list. Press enter with nothing inputted"
                             " to stop adding to your list.\n")
        if element == "":
            list_finished = True
            continue
        element = int_checker_after_question(element)
        list_of_elements.append(element)

    index_required = len(list_of_elements) - mth_to_last
    if int(index_required) < 0:
        print("NIL")
    else:
        print(list_of_elements[index_required])

def int_checker(user_question):
    while True:
        try:
            return_value = int(input(user_question))
            break
        except Exception:
            print("That isn't an integer. Try again!")
    return return_value

def int_checker_after_question(element):
    while True:
        try:
            return_value = int(element)
            break
        except Exception:
            print("That isn't an integer. Type another element in your list!")
            element = input()
    return return_value


element_from_last()




