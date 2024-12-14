ville = ""
ville_tab=[]
ville_tab_population=[]

while ville.lower() != "stop":
    ville = input("donner le nom de la ville :\n ")
    ville_tab.append(ville)
dernier_ville = ville_tab.pop()
for ville_ in ville_tab:
    taille =len(ville_) 
    population=taille*1000000
    ville_tab_population.append((ville_,population))
ville_tab_population.sort(key=lambda x: x[1], reverse=True) 
print("Villes triées par population (du plus grand au plus petit) :")
for ville_, population in ville_tab_population:
    print(f"{ville_} - Population: {population}")

  

    
    
