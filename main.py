"""
main.py
-------

Main program for GeneInsight.

Author: Roshni Kathiresan
Project: GeneInsight
Version: 3.0
"""

from src.validator import validate_sequence
from src.nucleotide_counter import count_nucleotides
from src.gc_content import calculate_gc_content
from src.reverse_complement import reverse_complement
from src.transcription import transcribe_dna
from src.translation import translate_rna
from src.orf import find_orf
from src.fasta_reader import read_fasta
from src.restriction_sites import find_restriction_sites
from src.report import generate_report


def main():
    """
    Runs the GeneInsight DNA analysis pipeline.
    """

    print("=" * 60)
    print("🧬        Welcome to GeneInsight        🧬")
    print("=" * 60)

    # -----------------------------
    # Input Method
    # -----------------------------
    print("\nChoose Input Method")
    print("1. Enter DNA sequence manually")
    print("2. Read from FASTA file")

    choice = input("\nEnter choice (1/2): ")

    if choice == "1":
        sequence = input("\nEnter DNA Sequence: ").strip().upper()

    elif choice == "2":
        file_path = input("\nEnter FASTA file path: ")

        try:
            sequence = read_fasta(file_path)
        except FileNotFoundError:
            print("\n❌ FASTA file not found.")
            return

    else:
        print("\n❌ Invalid choice.")
        return

    # -----------------------------
    # Validate DNA
    # -----------------------------
    if not validate_sequence(sequence):
        print("\n❌ Invalid DNA Sequence!")
        print("Only A, T, G and C are allowed.")
        return

    # -----------------------------
    # Analysis
    # -----------------------------
    counts = count_nucleotides(sequence)

    gc_content = calculate_gc_content(counts)

    reverse = reverse_complement(sequence)

    rna = transcribe_dna(sequence)

    protein = translate_rna(rna)

    orf = find_orf(rna)

    restriction_sites = find_restriction_sites(sequence)

    # -----------------------------
    # Save Report
    # -----------------------------
    generate_report(
        sequence,
        counts,
        gc_content,
        reverse,
        rna,
        protein,
        orf,
        restriction_sites
    )

    # -----------------------------
    # Display Report
    # -----------------------------
    print("\n" + "=" * 60)
    print("                DNA ANALYSIS REPORT")
    print("=" * 60)

    print(f"\nOriginal DNA          : {sequence}")

    print("\nNucleotide Counts")
    print("-" * 25)

    for base, count in counts.items():
        print(f"{base} : {count}")

    print(f"\nGC Content            : {gc_content}%")
    print(f"Reverse Complement    : {reverse}")
    print(f"RNA Sequence          : {rna}")
    print(f"Protein Sequence      : {protein}")
    print(f"First ORF             : {orf}")

    print("\nRestriction Enzyme Sites")
    print("-" * 25)

    for enzyme, positions in restriction_sites.items():
        if positions:
            print(f"{enzyme:<10}: {positions}")
        else:
            print(f"{enzyme:<10}: Not Found")

    print("\n📄 Report saved successfully!")
    print("Location : output/report.txt")

    print("\n" + "=" * 60)
    print("✅ Analysis Completed Successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()