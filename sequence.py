import numpy as np

class Sequence():
    "A simple attempt to model a DNA sequence"
    "Available methods \n count, is_valid, nonpair, comp, genes and mutation "

    def __init__(self, sequence, which = "DNA", is_valid = None):
        "Initialize sequence, which (default = 'DNA') and is_valid (default = None)"
        self.__which = which.upper()
        if self.__which == "DNA":
            self.__nucleotides = ("A", "C", "G", "T")
            self.__complement = { "A":"T", "T":"A", "G":"C", "C":"G"}
        elif self.__which == "RNA":
            self.__nucleotides = ("A", "C", "G", "T", "U")
            self.__complement = { "A":"T", "T":"A", "G":"C", "C":"G", "U":"T"}
        self.__sequence = np.array(list(sequence.upper()))
        self.__is_valid = is_valid

    def count(self):
        "Counts the number of nucleotides"
        sequence_count = np.count_nonzero(self.__sequence)
        return sequence_count

    def validate(self):
        "Checks if all the nucleotides are viable depending on which"
        boolean_list = []
        for i in range(self.__sequence.shape[0]):
            if self.__sequence[i] in self.__nucleotides:
                boolean_list.append(True)
            else:
                boolean_list.append(False)
        #Stores true if all the elements in list contains True bool
        is_valid = all(boolean for boolean in boolean_list)
        if is_valid:
            self.__is_valid = True
        #Else it will return False
        return is_valid

    def __eq__(self,other):
            "returns true if x == y"
            #Checks if both compared instances belong to the same class
            if isinstance(self,Sequence) and isinstance(other,Sequence):
                return np.array_equal(self.__sequence,other.__sequence)
            else:
                print("Compared objects are not of the same class")

    def comp(self):
        "Returns the complement as a new Sequence instance"
        #list comprehension reads as: for each nucleotide in the sequence pick
        #its complementary from the corresponding dictionary
        comp_string = np.array([self.__complement[nucleotide] for nucleotide in self.__sequence])
        return Sequence(''.join(comp_string))


    def nonpair(self,other):
        "Finds the first pair of non-matching bases when comparing two"
        "sequences"
        if len(range(self.__sequence.shape[0])) != len(range(other.__sequence.shape[0])):
            raise Exception('Can not compare sequences of different lengths')
        not_found = True
        while not_found:
            for i in range(self.__sequence.shape[0]):
                if self.__sequence[i] != other.__sequence[i]:
                    not_found = False
                    return i
                elif i == len(range(self.__sequence.shape[0]))-1:
                    not_found = False
                    return -1

    def genes(self):
        "Finds and splits the genes in the genome storing them as Sequence instances"
        genome_str = "".join(self.__sequence)
        #genes list will store Sequence instances for each gene
        genes = []
        try:
            gene = genome_str.split("AAAAAAAAAATTTTTTTTTT")
        except:
            print("Your genome has no 'full stops'")
            gene = list(genome_str)
        for i in range(len(gene)):
            genes.append(Sequence(gene[i]))
        return genes

    def mutation(self,other):
        "Finds the number of mutations between two Sequence instances"
        counter = 0
        for i in range(self.__sequence.shape[0]):
            if self.__sequence[i] != other.__sequence[i]:
                counter += 1
        return counter


    @property
    def sequence(self):
        return self.__sequence
    @property
    def is_valid(self):
        return self.__is_valid


def read(filename):
    with open(filename, 'r', encoding='ASCII') as datafile:
        next(datafile)
        genome = datafile.read()
    return Sequence(genome)
