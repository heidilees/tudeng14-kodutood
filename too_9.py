#!/usr/bin/env python3
"""
Programm, mis loeb valgu FASTA faili ja arvutab valgu molaarmassi, aminohapete arvu ja isoelektrilise punkti.
"""

__author__ = "Heidi Lees"
__copyright__ = "Copyright 2015, Minufirma"
__credits__ = ["Heidi Lees", "Taaniel Jakobson"]
__version__ = "0.001"
__email__ = "heidi_lees@hotmail.com"

from Bio import SeqIO
from Bio.SeqUtils.ProtParam import ProteinAnalysis
from Bio.Seq import Seq


def read_fasta(fasta): # loeb etteantud FASTA faili ja annab m6ned parameetrid
    for seq_record in SeqIO.parse(fasta, "fasta"):
        print("ID:",seq_record.id)
        print("Pikkus:",len(seq_record))
    return(seq_record.seq)
    
def main(): #programm, mis kysib valgu fasta faili ja annab selle kohta parameetrid
    fasta = input()
    sequence = read_fasta(fasta)
    print(sequence)
    analysed_seq = ProteinAnalysis(str(sequence))
    print("\n","Molekulaarmass:",analysed_seq.molecular_weight())
    print("\n","Aminohapete arv:",analysed_seq.count_amino_acids())
    print("\n","Isoelektriline punkt:",analysed_seq.isoelectric_point())
    text_file = open("Valgu_parameetrid.txt", "w")
    text_file.write(str(analysed_seq.molecular_weight()))
    text_file.write("\n")
    text_file.write(str(analysed_seq.count_amino_acids()))
    text_file.write("\n")
    text_file.write(str(analysed_seq.isoelectric_point()))
    text_file.close()



if __name__ == "__main__":
    main()




