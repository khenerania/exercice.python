import statistics
def save_list(user_list):
    filename = input("Enter filename to save the list: ")
    with open(filename, 'w') as file:
        for num in user_list:
            file.write("%s\n" % num)
    print(f"List saved to {filename}.")

def load_and_append_list():
    filename = input("Enter filename to load the list from: ")
    try:
        with open(filename, 'r') as file:
            loaded_list = [int(line.strip()) for line in file]
        user_list.extend(loaded_list)
        print(f"List loaded and appended from {filename}: {user_list}")
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
    except ValueError:
        print("Error: File contains non-integer values.")

user_list = []

while True:
    try:
        number = int(input("Enter a number (0 to stop): "))
        if number == 0:
            break
        user_list.append(number)
        print("Current List:", user_list)
        print("Sorted List (Ascending):", sorted(user_list))
        print("Sorted List (Descending):", sorted(user_list, reverse=True))
        mean = statistics.mean(user_list)
        median = statistics.median(user_list)
        print(f"Mean: {mean}, Median: {median}")
    except ValueError:
        print("Invalid input. Please enter an integer.")

print("Final Lists:")
print("Current List:", user_list)
print("Sorted List (Ascending):", sorted(user_list))
print("Sorted List (Descending):", sorted(user_list, reverse=True))

save_list(user_list)
load_and_append_list()
