#Number of genomes equals a number 
#of links between neurons

import random
hex_list = ['1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
gen_lifespam = 300
genome_length = 4

class Genome:
    def __init__(self):
        self.genes = []

    def generate_genome(self):
        for x in range(genome_length):
            self.genes.append([random.choice(hex_list)])
        return self.genes



   