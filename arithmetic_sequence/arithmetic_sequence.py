def generate_arithmetic_sequence(n, start=2, diff=3):
    """
    Generate an arithmetic sequence with `n` terms.
    
    :param n: Number of terms in the arithmetic sequence
    :param start: The first term of the sequence (default is 2)
    :param diff: The common difference between terms (default is 3)
    :return: List of numbers representing the arithmetic sequence
    """
    sequence = [start + i * diff for i in range(n)]
    return sequence

if __name__ == "__main__":
    n = int(input("Enter the number of terms in the sequence: "))
    result = generate_arithmetic_sequence(n)
    print(result)
