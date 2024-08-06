from Bio import SeqIO

# Specify the paths to the input files
info_file = "assembly_info.txt"  # The file containing the order information
fasta_file = "assembly.fasta"    # The original FASTA file
output_file = "reordered_assembly.fasta"  # The output FASTA file

# Read the order of sequences from the assembly_info.txt file
with open(info_file, "r") as f:
    order_lines = f.readlines()

# Extract sequence names from the assembly_info.txt file
order = []
for line in order_lines:
    if not line.startswith("#") and line.strip():  # Ignore comment and empty lines
        parts = line.strip().split("\t")
        seq_name = parts[0]  # Extract the sequence name
        order.append(seq_name)

# Read the sequences from the FASTA file
sequences = SeqIO.to_dict(SeqIO.parse(fasta_file, "fasta"))

# Reorder sequences according to the order list
reordered_sequences = [sequences[name] for name in order if name in sequences]

# Write the reordered sequences to a new FASTA file
SeqIO.write(reordered_sequences, output_file, "fasta")

print(f"Reordered sequences have been written to {output_file}")
