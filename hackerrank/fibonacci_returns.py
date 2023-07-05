import sys
def main():
    for num in sys.stdin:
        get_fibonacci_value(int(num))
        if int(num) <= -1:
            break

def get_fibonacci_value(nth_value):
    fib_list = [0, 1]
    for i in range(2, nth_value + 1):
        fib_list.append(fib_list[i-1] + fib_list[i-2])
    print(fib_list[nth_value])

main()