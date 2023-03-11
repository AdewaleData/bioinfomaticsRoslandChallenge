def count_nucleotides(dna_string):
    nucleotide_counts = {"A": 0, "C": 0, "G": 0, "T": 0}

    for nucleotide in dna_string:
        if nucleotide in nucleotide_counts:
            nucleotide_counts[nucleotide] += 1

    print("Number of A's:", nucleotide_counts["A"])
    print("Number of C's:", nucleotide_counts["C"])
    print("Number of G's:", nucleotide_counts["G"])
    print("Number of T's:", nucleotide_counts["T"])

    
'''You can call this function with a DNA string as the argument and it will print out the count of each nucleotide. For example
'''
    
count_nucleotides("ATCGGATTCGACTAGCTA")
    
'''This code defines a function reverse_complement that takes a DNA string as its argument. It creates a dictionary that maps each nucleotide to its complement, then uses a list comprehension to generate the complement of the DNA string. It then reverses the complement string using slicing and returns the reverse complement.

To use this function, you can call it with a DNA string as the argument, like this'''
    
