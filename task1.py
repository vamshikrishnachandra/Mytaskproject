def generate_fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_num = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_num)
    return fib_sequence

# Example usage:
num_terms = int(input())
fibonacci_sequence = generate_fibonacci(num_terms)
print("Fibonacci Sequence:")
print(fibonacci_sequence)
