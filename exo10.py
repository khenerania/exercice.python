# Demander à l'utilisateur d'entrer un mot
mot = input("Entrez un mot : ")

# Initialiser un indicateur pour vérifier si le mot est un palindrome
est_palindrome = True

# Parcourir le mot et comparer les caractères en utilisant l'indexation négative
for i in range(len(mot)):
    if mot[i] != mot[-(i + 1)]:
        est_palindrome = False
        break

# Afficher le résultat
if est_palindrome:
    print(f"Le mot '{mot}' est un palindrome.")
else:
    print(f"Le mot '{mot}' n'est pas un palindrome.")
