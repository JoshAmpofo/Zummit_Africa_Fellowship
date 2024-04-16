#!/usr/bin/env python3

"""
This script contains all the available DNA sequence analysis functions
"""

from Bio import SeqIO
from Bio.Seq import Seq
from helper_functions import file_opener
import sys

class DNASeq:
    """create class for DNA sequence analysis"""
   
    def check_seq_length(self, file):
        """
        checks length of DNA seq
        
        Arg(s):
            file (str or other file format): file containing DNA sequences
            
        Returns:
            int: length of DNA sequence
        """
        self.file = file
        if file.endswith(".fasta"):
            if sys.argv[1] in ["-m", "--multi"]:
                for record in SeqIO.parse(file, "fasta"):  #### SEARCH FOR A WAY TO VERIFY THAT A SEQUENCE FILE IS MULTI OR SINGLE
                    print(f"Sequence_id: {record.id}")
                    print(f"Length of Sequence is: {len(record):,} bp")
            elif sys.argv[1] in ['-s', '--single']:
                result = SeqIO.read(file, "fasta")
                return f"Length of sequence is: {len(result):,} bp"
        elif file.endswith(".gbk"):
            if sys.argv[1] in ["-m", "--multi"]:
                for record in SeqIO.parse(file, "genbank"):
                    print(f"Sequence id: {record.id}")
                    print(f"Length of Sequence is: {len(record):,} bp")
            elif sys.argv[1] in ['-s', '--single']:
                result = SeqIO.read(file, "genbank")
                return f"Length of sequence is: {len(result):,} bp"
        elif file.endswith(".txt"):
            return f"Length of Sequence is: {len(Seq(file_opener(file))):,} bp"
        else:
            return "Not a valid file format"


    def count_orf(file): ...


    def gc_content_one(file): ...


    def gc_content_three(file): ...
    


def main():
    file = sys.argv[2]
    dna = DNASeq()
    results = dna.check_seq_length(file)
    print(results)
    #print(file)
    

if __name__ == "__main__":
    main()