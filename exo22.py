def print_with_stars(string):
   
    for char in string:
        print(char)
        print("*")

def main():
    
    user_string = input("Please type in a string: ")
    print_with_stars(user_string)

if __name__ == "__main__":
    main()
