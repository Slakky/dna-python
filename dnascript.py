from sequence import Sequence, read
import matplotlib.pyplot as plt

class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

########SEQUENCES#######

my_sequence1 = Sequence("ACTG", "DNA")
my_sequence1_comp = Sequence("TGAC", "DNA")
my_sequence2 = Sequence("CGTAACTG", "DNA")
my_sequence3 = Sequence("ACTGX", "DNA")
my_sequence4 = Sequence("ACTG", "DNA")
my_sequence5 = Sequence("ATTG", "DNA")
my_sequence6 = Sequence("actg", "DNA")
my_sequence7 = Sequence("ACUG", "RNA")
my_sequence8 = Sequence("ACUGX", "RNA")

########TASK 1 EXAMPLE#######

print(Colors.HEADER + "\n- - - - - - - - TASK 1 - - - - - - - - " + Colors.ENDC)
print("\nUsed sequences in this example: ")
#From now on, in order to call an attribute of the instance (since those are
#private now) it will be called as follows: .'attribute'
print("\nmy_sequence1: {}" .format("".join(my_sequence1.sequence)))
print("\nmy_sequence2: {}" .format("".join(my_sequence2.sequence)))
print("\nClass of my_sequence1: {}".format(type(my_sequence1)))
print("\nClass of my_sequence2: {}".format(type(my_sequence2)))

#######TASK 2 EXAMPLE#######

print(Colors.HEADER + "\n- - - - - - - - TASK 2 - - - - - - - - " + Colors.ENDC)

print("\nUsed sequences in this example: ")
print("\nmy_sequence1: {}" .format("".join(my_sequence1.sequence)))
print("\nmy_sequence2: {}" .format("".join(my_sequence2.sequence)))

print("\nNumber of DNA bases of my_sequence1: {}".format(my_sequence1.count()))
print("\nNumber of DNA bases of my_sequence2: {}".format(my_sequence2.count()))

#######TASK 3 EXAMPLE#######


print(Colors.HEADER + "\n- - - - - - - - TASK 3 - - - - - - - - " + Colors.ENDC)

print("\nUsed sequences in this example: ")
print("\nmy_sequence1: {}" .format("".join(my_sequence1.sequence)))
print("\nmy_sequence3: {}" .format("".join(my_sequence3.sequence)))

print("\nIs my_sequence1 a valid nucleotide sequence?: {}".format(my_sequence1.validate()))
print("\nIs my_sequence3 a valid nucleotide sequence?: {}".format(my_sequence3.validate()))
print("\nNow I'm going to test it with" + Colors.OKBLUE + " assert" + Colors.ENDC +
" statements")

assert(my_sequence1.is_valid == True)
print(Colors.OKGREEN + "\nAs expected, we can assert my_sequence1.is_valid is True!" + Colors.ENDC)
try:
    assert(my_sequence3.is_valid == True)
except:
    print(Colors.FAIL + "\nAs expected, we can't assert my_sequence3.is_valid is True!"
    + Colors.ENDC)

#######TASK 4 EXAMPLE#######

print(Colors.HEADER + "\n- - - - - - - - TASK 4 - - - - - - - - " + Colors.ENDC)

print("\nUsed sequences in this example: ")
print("\nmy_sequence1: {}" .format("".join(my_sequence1.sequence)))
print("\nmy_sequence4: {}" .format("".join(my_sequence4.sequence)))
print("\nmy_sequence5: {}" .format("".join(my_sequence5.sequence)))

print("\nIs my_sequence1 == my_sequence4?: {}".format(my_sequence1 == my_sequence4))
print("\nIs my_sequence1 != my_sequence5?: {}".format(my_sequence1 != my_sequence5 ))
print("\nIs my_sequence1, my_sequence4?:   {}".format(my_sequence1 is my_sequence4))

#######TASK 5 EXAMPLE#######

my_sequence1comp = my_sequence1.comp()

print(Colors.HEADER + "\n- - - - - - - - TASK 5 - - - - - - - - " + Colors.ENDC)

print("\nUsed sequences in this example: ")
print("\nmy_sequence1comp: {}" .format("".join(my_sequence1comp.sequence)))
print("\nmy_sequence1_comp: {}" .format("".join(my_sequence1_comp.sequence)))

print("\nIs my_sequence1comp == my_sequence1_comp?: {}".format(my_sequence1comp == my_sequence1_comp))

#######TASK 6 EXAMPLE#######


print(Colors.HEADER + "\n- - - - - - - - TASK 6 - - - - - - - - " + Colors.ENDC)

print("\nUsed sequences in this example: ")
print("\nmy_sequence1: {}" .format("".join(my_sequence1.sequence)))
print("\nmy_sequence4: {}" .format("".join(my_sequence4.sequence)))
print("\nmy_sequence5: {}" .format("".join(my_sequence5.sequence)))


print("\nIs my_sequence4 == my_sequence5?: {}".format(my_sequence4 == my_sequence5))
print("\nIn which position can we find the first missmatch?: {}".format(my_sequence4.nonpair(my_sequence5)))
print("\nIs my_sequence4 == my_sequence1?: {}".format(my_sequence4 == my_sequence1))
print("\nWhat does the method return if we try to find the first missmatch?: {}".format(my_sequence4.nonpair(my_sequence1)))

#######TASK 7 EXAMPLE#######

print(Colors.HEADER + "\n- - - - - - - - TASK 7 - - - - - - - - " + Colors.ENDC)

print("\nUsed genomes in this example: ")
print("\ngenome_01: 'genome_01.dat'")

genome_01 = read("genome_01.dat")
print("\nOnce we've read the file, genome_01 is stored as: {}".format(type(genome_01)))
print("\nTherefore, we can access its attributes: ")
print("\ngenome_01 sequence: {}".format(genome_01.sequence))
print("\nHow many bases does the genome have?: {}".format(genome_01.count()))

#######TASK 8 EXAMPLE#######

print(Colors.HEADER + "\n- - - - - - - - TASK 8 - - - - - - - - " + Colors.ENDC)

print("\nUsed genomes in this example: ")
print("\ngenome_01: 'genome_01.dat'")

genes_01 = genome_01.genes()
genes_01_lengths = [gene.count() for gene in genes_01]

print("\nLength of the first gene: {}".format(genes_01_lengths[0]))

#######TASK 9 EXAMPLE#######

print(Colors.HEADER + "\n- - - - - - - - TASK 9 - - - - - - - - " + Colors.ENDC)

print("\nUsed genomes in this example: ")
print("\ngenome_01: 'genome_01.dat'")


plt.hist(genes_01_lengths, color = 'blue')
plt.xlabel("Number of bases")
plt.ylabel("Frequency")
plt.title('Gene length in genome_01.dat histogram')
plt.savefig("genome_01len.png")
plt.show()

#######TASK 10 EXAMPLE#######

print(Colors.HEADER + "\n- - - - - - - - TASK 10 - - - - - - - - " + Colors.ENDC)

print("\nUsed genomes in this example: ")
print("\ngenome_02: 'genome_02.dat'")

genome_02 = read("genome_02.dat")
genes_02 = genome_02.genes()
genes_02_lengths = [gene.count() for gene in genes_02]
gene_mutations = [gene.mutation(genes_02[i]) for gene,i in zip(genes_01,range(len(genes_02)))]

plt.scatter(genes_02_lengths, gene_mutations, marker = '.', color = 'blue')
plt.xlabel('Gene length')
plt.ylabel('Swap mutations')
plt.title('Genome_01 vs Genoma_02 mutation scatter plot')
plt.savefig("genome_02mutation.png")
plt.show()

#######TASK 11 EXAMPLE#######

print(Colors.HEADER + "\n- - - - - - - - TASK 11 - - - - - - - - " + Colors.ENDC)

print("\nUsed sequences in this example: ")
print("\nmy_sequence1: {}" .format("".join(my_sequence1.sequence)))
print("\nmy_sequence6: {}" .format("".join(my_sequence6.sequence).lower()))

print("\nCan we assert my_sequence1 == my_sequence6 although they have differente case?: ")

try:
    assert (my_sequence1 == my_sequence6)
    print(Colors.OKGREEN + "\nAs expected, we can assert my_sequence1 ==  my_sequence6"
    + Colors.ENDC)
except:
    print(Colors.FAIL + "\nWe can't assert my_sequence1 ==  my_sequence6"
    + Colors.ENDC)

#######TASK 13 EXAMPLE#######

print(Colors.HEADER + "\n- - - - - - - - TASK 13 - - - - - - - - " + Colors.ENDC)

print("\nUsed sequences in this example: ")
print("\nmy_sequence7: {}" .format("".join(my_sequence7.sequence)))
print("\nmy_sequence8: {}" .format("".join(my_sequence8.sequence)))

print("\nIs my_sequence7 a valid nucleotide sequence?: {}".format(my_sequence7.validate()))
print("\nIs my_sequence8 a valid nucleotide sequence?: {}".format(my_sequence8.validate()))

print(Colors.WARNING + "\nAlthough it makes no biological sense to complement a RNA sequence" +
" \nhere I'm going to test the corresponding method on a RNA sequence"+ Colors.ENDC)

my_sequence7comp = my_sequence7.comp()

print("\nmy_sequence7comp: {}" .format("".join(my_sequence7comp.sequence)))
