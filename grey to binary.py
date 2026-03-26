#just need to take xopr opertion of current number and its next number 

def gray_to_binary(n):
    # Start with the Gray code
    binary = n
    
    # Keep shifting right and XORing until no bits are left
    # This simulates the cumulative XOR chain
    while n > 0:
        n >>= 1
        binary ^= n
        
    return binary

# --- Testbench ---
# Binary 7 (111) -> Gray is 4 (100)
# Let's convert Gray 4 back to Binary
gray_val = 0b100 
result = gray_to_binary(gray_val)

print(f"Gray:   {bin(gray_val)} ({gray_val})")
print(f"Binary: {bin(result)} ({result})") # Expect 0b111 (7)
