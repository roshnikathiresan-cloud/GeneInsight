"""
orf_finder.py
-------------

Provides functions to identify the first Open Reading Frame (ORF)
in an RNA sequence.

Author: Roshni Kathiresan
Project: GeneInsight
Version: 1.0
"""
def find_orf(rna):
    """
    Finds the first Open Reading Frame (ORF) in an RNA sequence.

    Parameters:
        rna (str): RNA sequence.

    Returns:
        str: ORF sequence.
    """

    start = rna.find("AUG")

    if start == -1:
        return "No Start Codon Found"

    stop_codons = ["UAA", "UAG", "UGA"]

    orf = ""

    for i in range(start, len(rna), 3):

        codon = rna[i:i+3]

        if len(codon) != 3:
            break

        orf += codon

        if codon in stop_codons:
            break

    return orf