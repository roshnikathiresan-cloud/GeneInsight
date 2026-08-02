"""
translation.py
--------------

Provides functions to translate RNA into a protein sequence.

Author: Roshni Kathiresan
Project: GeneInsight
Version: 1.0
"""
def translate_rna(rna):
    """
    Translates an RNA sequence into a protein sequence.

    Parameters:
        rna (str): RNA sequence.

    Returns:
        str: Protein sequence.
    """
    rna = rna.upper()

    codon_table = {

        # Phenylalanine
        "UUU": "F", "UUC": "F",

        # Leucine
        "UUA": "L", "UUG": "L",
        "CUU": "L", "CUC": "L",
        "CUA": "L", "CUG": "L",

        # Isoleucine
        "AUU": "I", "AUC": "I",
        "AUA": "I",

        # Methionine (Start)
        "AUG": "M",

        # Valine
        "GUU": "V", "GUC": "V",
        "GUA": "V", "GUG": "V",

        # Serine
        "UCU": "S", "UCC": "S",
        "UCA": "S", "UCG": "S",
        "AGU": "S", "AGC": "S",

        # Proline
        "CCU": "P", "CCC": "P",
        "CCA": "P", "CCG": "P",

        # Threonine
        "ACU": "T", "ACC": "T",
        "ACA": "T", "ACG": "T",

        # Alanine
        "GCU": "A", "GCC": "A",
        "GCA": "A", "GCG": "A",

        # Tyrosine
        "UAU": "Y", "UAC": "Y",

        # Histidine
        "CAU": "H", "CAC": "H",

        # Glutamine
        "CAA": "Q", "CAG": "Q",

        # Asparagine
        "AAU": "N", "AAC": "N",

        # Lysine
        "AAA": "K", "AAG": "K",

        # Aspartic Acid
        "GAU": "D", "GAC": "D",

        # Glutamic Acid
        "GAA": "E", "GAG": "E",

        # Cysteine
        "UGU": "C", "UGC": "C",

        # Tryptophan
        "UGG": "W",

        # Arginine
        "CGU": "R", "CGC": "R",
        "CGA": "R", "CGG": "R",
        "AGA": "R", "AGG": "R",

        # Glycine
        "GGU": "G", "GGC": "G",
        "GGA": "G", "GGG": "G",

        # Stop Codons
        "UAA": "*",
        "UAG": "*",
        "UGA": "*"
    }

    protein = ""

    for i in range(0, len(rna), 3):

        codon = rna[i:i+3]

        if len(codon) != 3:
            break

        amino_acid = codon_table.get(codon, "X")

        if amino_acid == "*":
            break

        protein += amino_acid

    return protein