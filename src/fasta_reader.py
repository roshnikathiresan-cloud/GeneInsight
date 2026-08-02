"""
fasta_reader.py
---------------

Provides functions to read DNA sequences from FASTA files.

Author: Roshni Kathiresan
Project: GeneInsight
Version: 1.0
"""
def read_fasta(file_path):
    """
    Reads a FASTA file and returns the DNA sequence.

    Parameters:
        file_path (str): Path to FASTA file.

    Returns:
        str: DNA sequence.
    """
    sequence = ""
    with open(file_path, "r") as file:

        for line in file:

            line = line.strip()

            if line.startswith(">"):
                continue

            sequence += line

    return sequence.upper()