def ones_complement(number , bit_length):

# f"" an f string meaning expressions can be embedded into it
# number : the number being formatted , it should be an integer
# 0 : if the binary length is short the space be filled with zero
# b :  the number to binary format rep
# bit _length : the length of the binary number
    binary_rep = f"{number:0{bit_length}b}"

    one_complement = ''.join('1' if bit == '0' else '0' for bit in binary_rep)
    return one_complement

Complement = ones_complement(10,8)
print(Complement)