#!/usr/bin/env python3

from functools import reduce

"""
Advent of Code 2017 - Day 10
"""

def hash_list(inputs, pos=0, sk=0, sequ=[ i for i in range(256) ]):
    """the 'hashing algorithm'
    1) create variables and a list of ascending numbers
    2) sublist of num of elements from the inputs reversed
    3) set new current_position and step size
    """
    current_position, skip = pos, sk
    sequence = sequ

    for inp in inputs:

        # new sequence by reversing the subsequence of length inp
        sequence = construct_seq(sequence, current_position%len(sequence), inp)

        # set current_position and skip
        current_position += inp + skip
        skip += 1

    return sequence, current_position%len(sequence), skip


def construct_seq(seq, idx, num_elems):
    """construct the new sequence by reversing a subseq from i with num_elems elements"""
    revsubseq = list(reversed([ seq[(idx+i)%len(seq)] for i in range(num_elems) ]))
    # inserting the reversed elemets in the corresponding positions in the seq
    for i in range(num_elems):
        seq[(idx+i)%len(seq)] = revsubseq[i]
    return seq


def all_round_hash(fin):
    """
    1) convert each char in fin into its ascii represenation int + random extra values from the problem
    2) run the above alorithm 64times
    """
    bit_inp = [ ord(c) for c in fin ] + [17, 31, 73, 47, 23]
    preserved_inp = bit_inp.copy()
    pos, skip = 0, 0
    seq = [ i for i in range(256) ]

    for i in range(64):

        # reusing previous functions
        seq, pos, skip = hash_list(preserved_inp, pos=pos, sk=skip, sequ=seq)

    # making the hash denser
    # finally fixed, setting variables correctly, helps ...
    sparse_hash = seq
    dense_hash = dense_it_up(sparse_hash)

    return dense_hash

def dense_it_up(sparse):
    """making the sparse hash dense and return it"""
    dense = []
    for j in range(0,len(sparse),16):
        val = reduce(lambda a,b: a ^ b, sparse[j:j+16])
        hex_val = hex(val).replace('0x','')
        if len(hex_val) == 1: hex_val = '0'+hex_val
        dense.append(hex_val)
    return "".join(dense)


# START IT
if __name__ == "__main__":

    filename = "../testing_inputs/hash.txt"
    with open(filename) as inp:
        fin = inp.read().strip()
        inputs = [ int(n) for n in fin.split(",") ]

    hash_val, pos, skip = hash_list(inputs)
    print("The Hashvalue of the input is: {}".format(hash_val[0]*hash_val[1]))

    dense_bit_hash = all_round_hash(fin)
    print("The BitHashvalue of the inputs: {}".format(dense_bit_hash))
