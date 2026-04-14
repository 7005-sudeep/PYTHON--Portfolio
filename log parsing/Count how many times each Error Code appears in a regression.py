import re
from collections import defaultdict

def count_error_frequencies(file_path):
    # defaultdict(int) automatically starts counts at 0
    error_counts = defaultdict(int) # defaultdict using this only we cannot get any error if ddint in our list
    #
    try:
        with open(file_path, 'r') as file: # r= read mode also there are w= write mode and a=aapend mode (to overwrite or add new data)
            for line in file:
                # 1. Regex to find the Error Code (e.g., 'ERR_0x1A')
                match = re.search(r'ERR_0x[0-9A-Fa-f]+', line)
                
                if match:
                    error_code = match.group()
                    # 2. Add to scoreboard
                    error_counts[error_code] += 1
                    
        return error_counts
        
    except Exception as e:
        print(f"Error processing regression file: {e}")
        return None

# Usage
report = count_error_frequencies("regression_log.txt")
print(report)
# Output: {'ERR_0x1A': 50, 'ERR_0x2B': 12, 'ERR_0xCC': 5}
