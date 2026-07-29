from src.nucleotide_counter import count_nucleotides
from src.validator import validate_sequence
from src.gc_content import calculate_gc_content
from src.reverse_complement import reverse_complement
from src.transcription import transcribe_dna
sequence = input("Enter DNA Sequence: ").upper()

if validate_sequence(sequence):

    counts = count_nucleotides(sequence)

    gc = calculate_gc_content(counts)

    print("\nDNA Analysis Report")
    print("-" * 50)
    print("Sequence :", sequence)

    print("\nNucleotide Counts")

    for base, count in counts.items():
        print(f"{base} : {count}")

    print(f"\nGC Content : {gc}%")

else:
    print("❌ Invalid DNA sequence.")
    print("Only A, T, G and C are allowed.")
reverse = reverse_complement(sequence)
print(f"\nReverse Complement : {reverse}")
rna = transcribe_dna(sequence)
print(f"RNA Sequence : {rna}")