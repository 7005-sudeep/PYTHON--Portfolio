def binary_to_gray(n):
    # Logic: Gray = n XOR (n shifted right by 1)
    return n ^ (n >> 1)

# --- Test ---
# Binary 3 is 0b011
# 0b011 ^ 0b001 = 0b010 (Gray code for 3)
print(f"Gray code for 3: {bin(binary_to_gray(3))}")
