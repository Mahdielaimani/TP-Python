
import random
#{'question':'Claculer 23*6', 'reponse' :70}
list_qestion=[{'Calculer 25*3-5':70,}, {'Calculer 12-8*2':-4,},{'Calculer 200-30*3':110,}]
questions=list(list_qestion.keys())
random.shuffle(questions)
print(question)
score=0
reponse = int(input("Entrer la reponse "))
for _ in range (3):
    if reponse.value in list_qestion:
        value=list_qestion[reponse]
        score+=10
        print(score)
else:
    print('E')


#exercice sur les fichiers mode terminal
#f=open('nomfichier.txt','r')
#b=f.read()
#f=open('nomfichier.txt','w')
#f.write("Bounjour\n")
#f.write("Python nom languge")
#f.close()
    