def fibonacci():
    nth_value = int(input())
    f0 = 0
    f1 = 1
    outlying_cases = False
    while outlying_cases == False:
        if nth_value == 0:
            fn = 0
            outlying_cases = True
            continue
        if nth_value == 1:
            fn = 1
            outlying_cases = True
            continue
        for i in range(2, nth_value + 1):
            fn = f1 + f0
            f0 = f1
            f1 = fn
        outlying_cases = True
    print(fn)

fibonacci()