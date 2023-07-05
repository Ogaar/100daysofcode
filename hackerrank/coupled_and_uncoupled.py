def find_uncoupled():
    coupled_numbers = input().split(", ")
    frequency_dict = {}
    for number in coupled_numbers:
        if number not in frequency_dict:
            frequency_dict[number] = 1
        else:
            frequency_dict[number] += 1
    print(min(frequency_dict, key=frequency_dict.get))

find_uncoupled()
