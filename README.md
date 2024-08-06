# Reorder Flye Assembly

The `reorder_flye_assembly` script is designed to reorder sequences in a FASTA file generated by Flye to match the order specified in the `assembly_info.txt` file. Typically, the `assembly_info.txt` file lists contigs from largest to smallest, but the `assembly.fasta` file may have the sequences in a different order. This script rearranges the sequences in the FASTA file to match the order in `assembly_info.txt`.

## Prerequisites

Ensure you have the following files in your working directory:

- `assembly_info.txt`: The file containing contig information sorted from largest to smallest.
- `assembly.fasta`: The FASTA file with sequences to be reordered.

## Usage

Run the script in a Python environment. The output will be a new FASTA file named `reordered_assembly.fasta` with sequences ordered as specified in `assembly_info.txt`.

```bash
python reorder_flye_assembly.py
```
## Why, you may ask?

Well, I work in a diagnostic laboratory where unknowns are common. A metagenomic sequencing approach is sometimes the best approach. If we are lucky enough to get high quality DNA sequences and the de novo assembly is successful, grabbing the largest contig and BLASTing it will give us a lead as to what is most likely in the sample. Sometimes.
