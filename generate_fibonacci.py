""" This is a class model to generate fibonacci """


def generate_fibonacci(n):
    """
    Generates the Fibonacci sequence up to n terms.
    Args:
        n (int): The number of terms to generate.
    Returns:
        list: A list containing the Fibonacci sequence.
    """
    fib_sequence = [0, 1]  # Initialize with the first two terms
    while len(fib_sequence) < n:
        next_term = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_term)
    return fib_sequence


def main():
    try:
        num_terms = int(input("Number of Fibonacci terms to generate: "))
        if num_terms <= 0:
            print("Please enter a positive integer.")
            return
        fibonacci_sequence = generate_fibonacci(num_terms)
        print(f"The first {num_terms} terms of the Fibonacci sequence are:")
        print(fibonacci_sequence)
    except ValueError:
        print("Invalid input. Please enter a valid positive integer.")


if __name__ == "__main__":
    main()
