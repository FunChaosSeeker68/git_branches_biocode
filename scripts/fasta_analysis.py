def read_fasta(filename):
    seq = ""
    AT=0
    with open(filename) as f:
        for line in f:
            if not line.startswith(">"):
                seq += line.strip()
        for letter in seq:
            if letter == "A" or letter == "T":
                AT=AT+1

    print(AT/len(seq)*100)
    return seq

sequence = read_fasta("data/sequence.fasta")
print(sequence)
