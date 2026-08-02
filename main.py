from src.validator import validate_sequence
from src.nucleotide_counter import count_nucleotides
from src.gc_content import calculate_gc_content
from src.reverse_complement import reverse_complement
from src.transcription import transcribe_dna
from src.translation import translate_rna


def main():
    """
    Runs the GeneInsight DNA analysis pipeline.
    """

    print("=" * 50)
    print("🧬 Welcome to GeneInsight 🧬")
    print("=" * 50)

    sequence = input("\nEnter DNA Sequence: ").strip().upper()

    # Validate DNA
    if not validate_sequence(sequence):
        print("\n❌ Invalid DNA Sequence!")
        print("Only A, T, G and C are allowed.")
        return

    # Analysis
    counts = count_nucleotides(sequence)

    gc_content = calculate_gc_content(counts)

    reverse = reverse_complement(sequence)

    rna = transcribe_dna(sequence)

    protein = translate_rna(rna)

    # Report
    print("\n" + "=" * 50)
    print("           DNA ANALYSIS REPORT")
    print("=" * 50)

    print(f"\nOriginal DNA        : {sequence}")

    print("\nNucleotide Counts")
    print("------------------")

    for base, count in counts.items():
        print(f"{base} : {count}")

    print(f"\nGC Content          : {gc_content}%")

    print(f"Reverse Complement  : {reverse}")

    print(f"RNA Sequence        : {rna}")

    print(f"Protein Sequence    : {protein}")

    print("\n" + "=" * 50)
    print("Analysis Completed Successfully ✅")
    print("=" * 50)


if __name__ == "__main__":
    main()