#!/usr/bin/env python3

def print_fibonacci(length):
    if length <= 0:
        print([])
        return
    elif length == 1:
        print([0])
        return

    # Generate the Fibonacci sequence
    fibonacci = [0, 1]
    while len(fibonacci) < length:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    
    print(fibonacci)
