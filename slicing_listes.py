numbers=[1,2,3,4,5,6,7]

numbers.insert(4,0)
numbers[2]=22
numbers[2:2]=[33]
print(numbers)

import random
code =list(range(5))
print(code)

my_list = [random.randint(0, 9) for _ in range(3)]
print(my_list)

# Créer une liste de taille 3 avec des éléments uniques choisis aléatoirement entre 0 et 9
my_list = random.sample(range(10), 5)
print(my_list)
