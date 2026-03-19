from Point import Point
from algo import *


#### Série de tests pour l'exemple
a = Point(3,5)
b = Point(4,6)
c = Point(5,7)
d = Point(8,9)
e = Point(10,11)
f = Point(12,13)
g = Point(13,14)

path1 = [a,b,c,d,e,f,g]
path2 = [a,d,e,f,g,b,c]
path3 = [a,f,g,e,b,c,d]
path4 = [a,e,f,g,c,b,d]
path5 = [a,c,e,f,g,b,d]

population = [path1,path2,path3,path4,path5]

newparents = selection(population, False)

enfant_test1 = crossover(newparents)
print(enfant_test1)
enfant_mute = mutation(enfant_test1)
print(enfant_mute)
enfant_test2 = crossover(newparents)
print(enfant_test2)
newenfants = (enfant_test1,enfant_test2)
print(newenfants)

print(population)
new_population(population,newenfants)
print(population)

#### Reste à créer l'algorithme génétique utilisant toutes les fonctions auxilliaires
