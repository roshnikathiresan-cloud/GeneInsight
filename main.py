from src.nucleotide_counter import count_nucleotides
from src.validator import validate_sequence
sequence = "ATGCGATAG"

if validate_sequence(sequence):
    counts = count_nucleotides(sequence)

    print("DNA Sequence :", sequence)
    print("Nucleotide Counts")

    for base, count in counts.items():
        print(f"{base} : {count}")

else:
    print("Invalid DNA Sequence")