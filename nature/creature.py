from genome import *

class Creature:
    def __init__(self):
        self.genome = generate_genome()
        self.age = 0
        self.coord = []
    
    def mutateGene(self):
        self.genome[random.randint(0,genome_length)] = list(random.choice(hex_list))
        return self

    def __repr__(self):
        return 'Genome: ' + str(self.genome)  +  ", Age: " + str(self.age) + ", Coord: " + str(self.coord)

