nombre_personne =int(input("donner le nombre de personne a transporte\n"))
nombre_personne_taxi=int(input("donner le nombre de personne dans une taxi\n"))
quotient=nombre_personne//nombre_personne_taxi
reste=nombre_personne%nombre_personne_taxi

if(reste<=nombre_personne_taxi and reste>0):
    resultat=quotient+1
    print("le nombre de taxi est :\n",resultat)
else:
    print("le nombre de taxi est :\n",quotient)
 

