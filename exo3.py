amount=float(input("donner le montant total d'achat\n"))
articles=int(input("donner le nombre des articles\n"))
jour=input("donner le jour\n")
if jour in ["samedi","dimanche"]:
    discount=0.2
else:
    discount=0.1
if amount>=5:
    discount += 0.05
resultat=amount*(1-discount)
print("le prix total apres la redution est \n",resultat)
   