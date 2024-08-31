#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        print([])
    elif length == 1:
        print([0])
    elif length == 2:
        print([0, 1])
    else:
        a = 0
        b = 1
        sequence = [a, b]
        for i in range(2, length):
            c = a + b
            a = b
            b = c
            sequence.append(b)
        print(sequence)