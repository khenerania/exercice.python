list=[1,2,3,4,5]
while True:
    index=int(input("donner l'index:\n"))
    if(index==-1):
        break
    else:
        valeur=int(input("donner la valeure:\n"))
        list.insert(index,valeur)
        print(list)
    