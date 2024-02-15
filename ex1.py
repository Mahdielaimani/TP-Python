import string
import random 
chaine=string.ascii_letters
numbers=string.digits
aliments=['fromage','chocolat','Confitur','jambon']
aliments[2:2]
print(aliments)
print(aliments[0])
aliments[2:2]="Miel"
print(aliments)
aliments[5:5]=["ketchup", "Saucisse"]
print(aliments)
aliments[2:8]=[]
print(aliments)
aliments[1:3]=['SALAD']
print(aliments)
