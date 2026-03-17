def read_fasta(filename):
    seq = ""
    with open(filename) as f:
        for line in f:
            if not line.startswith(">"):
                seq += line.strip()
    return seq

sequence = read_fasta("data/sequence.fasta")
print(sequence)
AT=0
sqw_num=len(sequence)
for letter in sequence:
    if letter == "A" or letter == "T":
        AT=AT+1
AT_PRECENT=(AT/sqw_num)*100
print (AT_PRECENT)