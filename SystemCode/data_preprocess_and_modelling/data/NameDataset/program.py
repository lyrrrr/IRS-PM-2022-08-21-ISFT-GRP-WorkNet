import random

with open('names.txt', 'r') as f:
    namesM = f.readlines()

with open('namesF.txt', 'r') as f:
    namesF = f.readlines()

with open('lastnames.txt', 'r') as f:
    lastnames = f.readlines()

morf = input('Masculino ou Feminino? (m/f): ')

if morf == 'm':
    name = random.choice(namesM) + ' ' + random.choice(lastnames)
elif morf == 'f':
    name = random.choice(namesF) + ' ' + random.choice(lastnames)

name = name.replace('\n', '')
print('Nome Gerado: ' + name)
