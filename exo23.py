def get_positive_integer():
   
    while True:
        try:
            n = int(input("Enter a positive integer N: "))
            if n > 0:
                return n
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def print_numbers(n):
    
    for i in range(-n, n + 1):
        if i != 0:
            print(i)

def main():
    
    n = get_positive_integer()
    print_numbers(n)

if __name__ == "__main__":
    main()
