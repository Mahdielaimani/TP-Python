'dict[nom]=(age,poids)'

person_dict = {}

person_dict = {'ALI': (22, 63), 'KHADIJA': (23,57)}

nom = input("Entrez un nom: ").upper()

if nom in person_dict:
    age, poids = person_dict[nom]
    print(f"Nom: {nom} ,Age: {age}, Poids: {poids}")
else:
    print("Ce nom n'existe pas dans le dictionnaire. ")