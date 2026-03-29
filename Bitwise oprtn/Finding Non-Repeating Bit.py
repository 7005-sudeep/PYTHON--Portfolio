# just using xor opertion as a xor a will give = 0

def find_unique_id(ids):
    accumulator = 0
    
    for val in ids:
        # XOR every value into the accumulator
        accumulator ^= val
        
    return accumulator

# --- Testbench ---
# IDs: 10, 25, 10, 42, 25
# 10 and 25 are pairs. 42 is the "Non-Repeating" bit.
data_stream = [10, 25, 10, 42, 25]
unique = find_unique_id(data_stream)

print(f"Data Stream: {data_stream}")
print(f"Unique ID:   {unique}") 
