numbers=[1,2,3,4,5]
while True:
    print("menue principale")
    print("1.Append")
    print("2.insert")
    print("3.pop")
    print("4.remove")
    print("5.sort")
    print("6.reverse")
    print("7.searche")
    print("8.save on the file ")
    print("9.load")
    print("10.quitter ")
    
    choix=int(input("choisissez une option\n"))
    if choix==1:
        element=int(input("donner un element a un inserer dans la liste\n"))
        numbers.append(element)
        print("liste:",numbers)
    elif choix==2:
        element=int(input("choisissez un element a inserer dans la liste\n"))
        indice=int(input("donner la position a inserer dans la liste\n"))
        numbers.insert(indice,element)
        print("liste :",numbers )
    elif choix==3:
        indice =int(input("donner l'indice de l'element a pop\n"))
        if(len(numbers)==0):
            print("on peut pas faire le pop\n")
        else:
            numbers.pop(indice)
            print("list:",numbers)
    elif choix==4:
        element=int(input(f"donner l'elment a  supprimer l'elemnt doit etre dans la liste voici la liste{numbers}\n"))
        if(len(numbers)==0):
            print("liste vide ")
        else:
            numbers.remove(element)
            print("liste:",numbers)
    elif choix==5:
       print("liste:",numbers.sort())
    elif choix==6:
        print("liste:",numbers.reverse())
    elif choix ==7:
        valeur = int(input("Enter value to search: "))
        if valeur in numbers:
           indice = numbers.indice(valeur)
           print(f"Valeur {valeur} trouver a l'indice {indice}.")
        else:
           print("Valeur n'existe pas.")
    elif choix==8:
         filename = input("donner e nom de fichier dont stocke la liste ")
         with open(filename, 'w') as file:
            for item in numbers:
               file.write("%s\n" % item)
            print(f"List sauvegarder dans  {filename}.")
    elif choix==9:
        filename = input("donner le fichier dont on charge la liste: ")
        try:
            with open(filename, 'r') as file:
                   loaded_list = [int(line.strip()) for line in file]
                   print(f"List charger de  {filename}: {loaded_list}")
        
        except FileNotFoundError:
           print(f"Error: {filename} not found.")
        except ValueError:
            print("Error: File contains non-integer values.")
    
    else:
        print("invalide choix\n")
