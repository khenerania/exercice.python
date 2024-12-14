print("runner 1:")
nom_1=input("donner votre nom:\n")
time_1=float(input("donner le temps passe en second :\n"))

print("runner 2:")
nom_2=input("donner votre nom:\n")
time_2=int(input("donner le temps passe en second :\n"))
if(time_1<time_2):
    print("le plus rapide est :",nom_1)
else:
    if(time_2<time_1):
        print("le plus rapide est :",nom_2)
    else:
        print("les deux ont passe le meme temps")