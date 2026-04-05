import re

# 1. Compile Pattern (Fast)
hex_regex = re.compile(r"0x[0-9a-f]+", re.IGNORECASE)

# 2. Open with safety flags
with open("huge_sim_log.log", "r", encoding='utf-8', errors='ignore') as f:
    for line in f:
        # 3. Find all hex values in the current line
        addresses = hex_regex.findall(line)
        
        if addresses:
            # 4. Do something with the addresses (e.g., print them)
            for addr in addresses:
                print(f"Found Address: {addr}")
