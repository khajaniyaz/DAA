def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y

    n = max(len(str(x)), len(str(y)))
    half_n = n // 2

    a = x // 10**half_n
    b = x % 10**half_n
    c = y // 10**half_n
    d = y % 10**half_n

    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    abcd = karatsuba(a + b, c + d)

    return (ac * 10**(2 * half_n)) + ((abcd - ac - bd) * 10**half_n) + bd

# Example usage
result = karatsuba(1234, 5678)
print(result)  # Output: 7006652
