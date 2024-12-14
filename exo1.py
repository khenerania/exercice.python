nom=input("entrer votre nom s'il vous plait\n")
if(nom=="VIP"):
    print("Enjoy the show for free!\n")
else:
    nombre_ticket=int(input("donner le nombre de ticket a acheter\n"))
    total=nombre_ticket*15.50
    print("le total est :",total)
    print("Enjoy your tickets!\n")