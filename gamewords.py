import random
list_mot=['programme','algorithme','procedure','python','modelisation']
mot=random.choice(list_mot)
print(mot)
mot1=list(mot)
random.shuffle(mot1)
print(mot1)
mot3=''.join(mot1)
tentative=0
print(mot3)
help_user=  input('les deux lettres sans pour vous helper: ')
while tentative <5:
  user_input=input('choisi le mot ')
  print(user_input)
  if mot == user_input:
    print("Success")
    break
  else:
    print("Bonne Courage a la prochine fois")
    tentative+=1
