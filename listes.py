numbers=[21,-15,12,5,7,32,32]

numbers.append(33)
print(numbers)


numbers.remove(5) # remove element
print(numbers)

numbers.pop(1) # remove element par index
print(numbers)

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

names=['mahdi', 'iman']

numbers.extend(names)
print(numbers)

numbers.extend(['Aya','Karim','Fouazia'])
print(numbers)

print(numbers.count(32))

del numbers[0:2]
print(numbers)

