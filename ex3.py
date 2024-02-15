mois = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']

jours= [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

i,j=1,0
while(len(mois)):
    mois[i:i]=[jours[j]]
    print(mois)
    i+=2 
    j+=1

