def reverse_bits(n, bit_width=8):
    result = 0
    
    for i in range(bit_width):
        # 1. Shift result LEFT to make room for the new bit
        result <<= 1
        
        # 2. "Pop" the LSB from input n (n & 1)
        # 3. "Push" it into the LSB of result using OR (|)
        result |= (n & 1)
        
        # 4. Shift input n RIGHT to get the next bit ready
        n >>= 1
        
    return result

# --- Testbench ---
# Input: 10110000 (Decimal 176)
# Expected Output: 00001101 (Decimal 13)
input_val = 0b10110000 
output_val = reverse_bits(input_val, 8)

print(f"Original: {bin(input_val)}")
print(f"Reversed: {bin(output_val).zfill(10)}") # zfill helps show the leading zeros


1. Why (n & 1)? (The "Sampler")
In Python (and hardware), 1 in binary is ...00000001.
When you use n & 1, the AND gate zeros out every single bit in n except for the very last one (the LSB).

If the LSB of n was 1: 1 & 1 results in 1.

If the LSB of n was 0: 0 & 1 results in 0.

This is how we "pop" or sample the bit without caring about the rest of the 32-bit number.

2. Why result |= ...? (The "Driver")
After you have shifted result to the left, its LSB is always a 0. We need to "set" that 0 to a 1 if our sampled bit was high.

The OR Gate Rule: 0 | 1 = 1 and 0 | 0 = 0.

Since the LSB of result is currently 0, using | effectively "copies" the sampled bit into that position.
