"""
nucleotide_counter.py
---------------------

This module counts the number of A, T, G, and C nucleotides
in a DNA sequence.

Author: Roshni Kathiresan
Project: GeneInsight
Version: 1.0
"""
def count_nucleotides(sequence):
    """
    Counts the number of A, T, G, and C nucleotides in a DNA sequence.

    Parameters:
        sequence (str): A validated DNA sequence.

    Returns:
        dict: Dictionary containing nucleotide counts.
    """
    sequence = sequence.upper()
    sequence = sequence.replace(" ", "")  
    counts = {"A": 0, "T": 0, "G": 0, "C": 0}
    for base in sequence:
        if base in counts:
            counts[base] += 1
    return counts