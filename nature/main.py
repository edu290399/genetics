from venv import create
from genome import Genome
from creature import Creature

world_size = [128,128]
population_size = 1024


def main():
    genome = Genome()
    population = []

    for x in range(population_size):
        creature = Creature()
        population.append(creature)
    print(population[0].genome)
    population[0].mutateGene()
    print(population[0].genome)

main()


