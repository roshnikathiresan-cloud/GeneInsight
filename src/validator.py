"""
validator.py
-------------
Module for validating DNA sequences.

Author: Roshni Kathiresan
Project: GeneInsight
"""
def validate_sequence(sequence):
    """
    Checks whether a DNA sequence contains only A, T, G and C.

    Parameters:
        sequence (str): DNA sequence entered by the user.

    Returns:
        bool: True if valid, False otherwise.
    """
    sequence = sequence.upper()
    sequence = sequence.replace(" ", "")  
    if len(sequence) == 0:
        return False
    valid_bases = {"A", "T", "G", "C"}
    for base in sequence:
        if base not in valid_bases:
            return False
    return True
