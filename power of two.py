def is_power_of_two(n):
    if n <= 0: return False
    # A power of 2 ANDed with its predecessor is always 0
    return (n & (n - 1)) == 0

print(f"Is 16 a power of 2? {is_power_of_two(16)}") # True
print(f"Is 18 a power of 2? {is_power_of_two(18)}") # False

1. Checking Odd/Even (n & 1)This only looks at the LSB (Least Significant Bit).If the LSB is 1, the number is Odd.
If the LSB is 0, the number is Even.
It doesn't care about any of the other bits (the "higher" wires).
2. Checking Power of Two (n & (n - 1))This looks at all the bits in the register. 
A power of two (like 2, 4, 8, 16) has a very specific "signature" in binary: it has exactly one bit set to 1
.NumberBinary (n)Binary (n−1)n & (n−1)Result
8 (Power of 2)100001111000 & 01110000 (Match!)
16 (Power of 2)100000111110000 & 0111100000 (Match!)
10 (Not Power)101010011010 & 10011000 (No Match)
