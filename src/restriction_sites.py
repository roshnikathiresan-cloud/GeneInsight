"""
restriction_sites.py
--------------------

Finds restriction enzyme recognition sites in a DNA sequence.

Author: Roshni Kathiresan
Project: GeneInsight
Version: 1.0
"""

def find_restriction_sites(sequence):
    """
    Finds restriction enzyme recognition sites.

    Parameters:
        sequence (str): DNA sequence

    Returns:
        dict: Enzyme names with cut positions.
    """

    sequence = sequence.upper()

    enzymes = {

        "EcoRI": "GAATTC",
        "BamHI": "GGATCC",
        "HindIII": "AAGCTT",
        "NotI": "GCGGCCGC",
        "XhoI": "CTCGAG",
        "PstI": "CTGCAG"

    }

    results = {}

    for enzyme, site in enzymes.items():

        positions = []

        start = 0

        while True:

            index = sequence.find(site, start)

            if index == -1:
                break

            positions.append(index + 1)   # 1-based indexing

            start = index + 1

        results[enzyme] = positions

    return results