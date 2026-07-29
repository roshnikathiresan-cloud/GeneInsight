"""
transcription.py
----------------

Provides functions to transcribe a DNA sequence into RNA.

Author: Roshni Kathiresan
Project: GeneInsight
Version: 1.0
"""
def transcribe_dna(sequence):
    """
    Converts a DNA sequence into RNA.

    Parameters:
        sequence (str): Valid DNA sequence.

    Returns:
        str: RNA sequence.
    """
    sequence = sequence.upper()
    rna_sequence = sequence.replace("T","U")
    return rna_sequence