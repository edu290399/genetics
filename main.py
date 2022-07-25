from nature.genome import Genome
from nature.creature import Creature

world_size = [128,128]
population = 1024


def main():
    creature = Creature()
    genome = Genome()
    genome.genes = genome.generate_genome()
    print(genome.genes)
    print(creature)
main()


