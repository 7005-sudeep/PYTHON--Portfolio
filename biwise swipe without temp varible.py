# here opertion is same as blockin statement in verilog 
def xor_swap(a, b):
    print(f"Before: a = {a}, b = {b}")
    
    a = a ^ b  # Combined state
    b = a ^ b  # b becomes original a
    a = a ^ b  # a becomes original b
    
    print(f"After:  a = {a}, b = {b}")
    return a, b

# --- Testbench ---
xor_swap(10, 20) 
# Binary 10: 1010
# Binary 20: 10100
