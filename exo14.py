
input_string = input("Entrez une chaîne de caractères : ")


width = 30


padding = (width - len(input_string)) // 2


line_middle = "." + " " * padding + input_string + " " * (width - len(input_string) - padding - 1) + "*"


print("le mot est :",input_string)
print(line_middle)

