import collections

Nucleotides = ["A","C","G","T"]

#Check sequence to ensure DNA is a string
def validateSeq(dna_seq):
    tmpseq = dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in Nucleotides:
            return False
    return tmpseq    

#Frequency of Bases

def countNucFrequency(seq):
    # tmpFreqDict = {"A": 0, "C": 0, "G": 0, "T": 0,}
    tmpFreqDict = {"A": 0, "C": 0, "G": 0, "T": 0,}
    for nuc in seq:
        tmpFreqDict[nuc] += 1
    return tmpFreqDict
    # return dict(collections.Counter(seq))
