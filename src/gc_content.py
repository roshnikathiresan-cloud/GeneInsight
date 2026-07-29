"""
gc_content.py
---------------------

This module calculates the GC content of a DNA sequence.

Author: Roshni Kathiresan
Project: GeneInsight
Version: 1.0
"""
def calculate_gc_content(counts):
    """
    Calculates the GC percentage.

    Parameters:
        counts (dict): Dictionary containing nucleotide counts.

    Returns:
        float: GC percentage.
    """

    total = sum(counts.values())

    if total == 0:
        return 0.0

    gc = counts["G"] + counts["C"]

    gc_percentage = (gc / total) * 100

    return round(gc_percentage, 2)