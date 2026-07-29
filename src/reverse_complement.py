"""
reverse_complement.py
---------------------

Provides functions to generate the reverse complement
of a DNA sequence.

Author: Roshni Kathiresan
Project: GeneInsight
Version: 1.0
"""
def reverse_complement(sequence):
    """
    Generates the reverse complement of a DNA sequence.

    Parameters:
        sequence (str): Valid DNA sequence.

    Returns:
        str: Reverse complement sequence.
    """
    sequence = sequence.upper()
    complement = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    complement_sequence = ""

    for nucleotide in sequence:
        complement_sequence += complement[nucleotide]

    reverse = complement_sequence[::-1]

    return reverse