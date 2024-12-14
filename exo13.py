while True:
    # Demander à l'utilisateur d'entrer une chaîne de caractères
    user_input = input("Entrez une chaîne de caractères (ou appuyez sur Entrée pour terminer) : ")
    
    # Vérifier si l'entrée est vide pour arrêter la boucle
    if user_input == "":
        break
    
    # Afficher la chaîne de caractères
    print(user_input)
    
    # Afficher une ligne de soulignement de la même longueur que la chaîne de caractères
    print('-' * len(user_input))
