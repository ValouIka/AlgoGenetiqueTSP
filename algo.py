import math
import operator
import random

import numpy as np
from Point import Point

#### Fonction de génération d'une population aléatoire de 5 individus de taille size
def generate_population(size):
    population = []
    for i in range(5):
        path = []
        point = None
        for j in range(size):
            while True:
                point = Point(random.randint(0,25),random.randint(0,25))
                if not point in path: break
            path += point
        population += path
    return population
        


#### Fonction d'évaluation de la taille d'un chemin
#### "path" est une liste de points
def path_length(path):
    pl = 0
    for i in range(1,len(path)):
        pl += path[i].distance(path[i-1])
    return pl


#### Fonction de sélection, qui choisit les parents de la prochaine génération.
#### Pour une population donnée, on choisit les deux parents ayant le plus court chemin.
#### Une population est définie comme une liste de chemin.
#### Si bad_ones = True, renvoie les deux plus mauvais individus à la place.
def selection(population, bad_ones):
    lengths_size = np.zeros(len(population[0]))
    for i in range(len(population)):
        lengths_size[i] = path_length(population[i])
    population_by_size = zip(population, lengths_size)
    if bad_ones:
        population_by_size = sorted(population_by_size, key=operator.itemgetter(1), reverse=False)
    else:
        population_by_size = sorted(population_by_size, key=operator.itemgetter(1), reverse=True)
    return population_by_size[0][0], population_by_size[1][0]

#### Fonction de crossover, qui combine les informations des deux parents pour créer
#### un nouvel individu.
#### On choisit une coupe aléatoire entre le premier élément et
#### le dernier, et on obtient deux segments.
#### On colle finalement le parent2 au premier segment du parent1, en supprimant
#### les doublons du parent2.
def crossover(parents):
    parent1 = parents[0]
    parent2 = parents[1]
    print(parent1)
    print(parent2)
    segment = parent1[0:random.randint(1,len(parent1)-1)]
    print(segment)
    parent2_to_append = [item for item in parent2 if item not in segment]
    return segment+parent2_to_append

#### Fonction de mutation, devant être utilisée selon une probabilité p.
#### Intervertit aléatoirement deux éléments aléatoires d'un chemin.

def mutation(path):
    a = random.randint(1,len(path)-1)
    b = random.randint(1,len(path)-1)
    temp = path[a]
    path[a] = path[b]
    path[b] = temp

#### Fonction de repopulation: les enfants remplacent en nombre égal les
#### plus mauvais individus de la population.
def new_population(population, children):
    bad_ones = selection(population, True)
    bad1 = population.index(bad_ones[0])
    bad2 = population.index(bad_ones[1])
    population[bad1] = children[0]
    population[bad2] = children[1]



