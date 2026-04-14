import re

def extract_and_convert(log_line):
    try:
        # 1. Isolate the part we want using Regex
        # Looking for '0x' followed by hexadecimal characters (0-9, A-F)
        match = re.search(r'0x[0-9A-Fa-f]+', log_line)
        
        if match:
            hex_string = match.group() # This gives us '0x1A'
            
            # 2. Convert to Integer (base 16)
            # Python's int() function is brilliant: the second argument 
            # tells it which base (number system) to use.
            value = int(hex_string, 16)
            
            return value
        
        return None
    except Exception as e:
        return f"Conversion failed: {e}"

# Test
log = "ERROR_DETECTED_at_ADDRESS_0x1A"
print(f"Decoded Value: {extract_and_convert(log)}") 
# Output: 26



#for the logs upto 1 gn we just use re.findall lib
import re

def process_huge_log(file_path):
    # 'with open' is safer because it automatically closes the file for you
    with open(file_path, 'r') as file:
        for line in file:  # <--- This is the secret!
            # Process one line at a time
            matches = re.findall(r'0x[0-9A-Fa-f]+', line)
            if matches:
                for hex_val in matches:
                    print(f"Found: {hex_val} -> {int(hex_val, 16)}")

# Usage: process_huge_log("simulation_output.log")
