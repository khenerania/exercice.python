annee=int(input("donner l'annee:\n"))
if (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0): 
    print(f"{annee} is a leap year.") 
else:
    print(f"{annee} is not a leap year.")
