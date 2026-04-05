# in this exapmple i will use impoer re libary as it scan the error for file
# and in that we have to use try-except method just like trial and error method₹

import re

def scan_for_fatal(file_path):
    # Pre-compiling the pattern makes it faster for a 1GB file
    # 'i' flag (IGNORECASE) is used because loggers sometimes use 'FATAL' or 'fatal'
    fatal_pattern = re.compile(r"Fatal", re.IGNORECASE)

    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
            for line_num, line in enumerate(file, 1):
                # Using re.search() as you suggested
                match = fatal_pattern.search(line)
                
                if match:
                    # Printing the line number and the matching line
                    print(f"[MATCH] Line {line_num}: {line.strip()}")
                    
    except FileNotFoundError:
        print("File not found. Check the path!")

# Run the scanner
scan_for_fatal("simulation_log.txt")
