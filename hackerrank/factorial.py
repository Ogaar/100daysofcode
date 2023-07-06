def get_factorial():
    n_input = int(input())
    list_between_n = list(range(1, n_input + 1))
    n_factorial = 1
    for number in list_between_n:
        n_factorial *= number
    print(n_factorial)

get_factorial()