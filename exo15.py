user_input = input("Please type in a string: ")
voyelles = ['a', 'e', 'o']
for voyelle in voyelles:
    if voyelle in user_input:
        print(f"{voyelle} found")
    else:
        print(f"{voyelle} not found")
