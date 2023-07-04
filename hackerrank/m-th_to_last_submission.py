
def main():
    m = int(input())
    list_of_elements = input().split(" ")
    index_required = len(list_of_elements) - m
    if index_required < 0:
        print("NIL")
    else:
        print(list_of_elements[index_required])

main()
