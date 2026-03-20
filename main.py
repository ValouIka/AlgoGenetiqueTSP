from Point import Point
from algo import *


#### Série de tests pour l'exemple
population = generate_population(10)

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
