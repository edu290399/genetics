#Number of genomes equals a number 
#of links between neurons

import random
hex_list = ['1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
gen_lifespam = 300
genome_length = 16

def generate_genome():
    genes = []
    for x in range(genome_length):
        genes.append([random.choice(hex_list)])
    return genes
class Genome:
    def __init__(self):
        self.genes = []
    
    def __repr__(self):
        return 'Genes: ' + str(self.genes)




   