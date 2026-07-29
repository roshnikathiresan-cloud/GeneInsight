from src.nucleotide_counter import count_nucleotides
from src.validator import validate_sequence
from src.gc_content import calculate_gc_content
sequence = input("Enter DNA Sequence: ")

if validate_sequence(sequence):

    counts = count_nucleotides(sequence)

    gc = calculate_gc_content(counts)

    print("\nDNA Analysis Report")
    print("-" * 30)
    print("Sequence :", sequence)

    print("\nNucleotide Counts")

    for base, count in counts.items():
        print(f"{base} : {count}")

    print(f"\nGC Content : {gc}%")

else:
    print("❌ Invalid DNA sequence.")
    print("Only A, T, G and C are allowed.")