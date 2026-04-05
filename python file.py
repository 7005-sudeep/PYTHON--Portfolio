Pillar 1: The "Hardware Data" (Arrays & Lists)
These test your ability to handle streams of transaction data.

Move Zeros to End: (We did this!) Squeezing out bubbles in a pipeline.//complete

Two Sum: (We did this!) Checking address pairs. //complete

Majority Element: (We did this!) Arbiter/Voting logic. //complete

Missing Number: (We did this!) Dropped packet detection.

Contains Duplicate: (We did this!) Scoreboard collision check.

Best Time to Buy/Sell Stock: Finding max delta (latency/throughput analysis). #complete

Rotate Array: Mimicking a circular buffer or barrel shifter. #complete

Merge Sorted Arrays: Combining two sorted data streams (Arbiter logic).#complete

Find the "Single" Number: Use XOR to find a non-repeated ID. #complete

Intersection of Two Arrays: Finding common addresses in two memory maps. #complete

Pillar 2: The "Bit-Smasher" (Bitwise Operations) #complete
This is the #1 skill for ASIC engineers. Python handles bits differently than Verilog!

Count Set Bits: Calculate parity (Hamming weight).# complete

Reverse Bits: Endianness conversion (Big-Endian to Little-Endian). #complete

Power of Two: Check if an address is aligned to a power of 2. #complete 

Bitwise Swap: Swap two numbers without a temp variable using XOR. #complete

Extract Bitfield: Given (val, high, low), extract specific bits. #complete

Isolate Rightmost Set Bit: Common in priority encoders. #complete

Gray Code to Binary: Converting sensor data or CDC pointers. #complete

Find the Non-Repeating Bit: XOR magic with multiple numbers. #complete

Check Parity: Return 1 if odd number of bits are set. #complete

Set/Clear/Toggle a Bit: Basic register manipulation. #complete

Pillar 3: The "Log Parser" (Strings & Files)


Search for "ERROR": Scan a 1GB file and print lines containing "Fatal".#complete

Extract Hex Values: Use Regular Expressions (Regex) to find all 0x addresses in a log.

Valid Palindrome: Checking if a data packet is symmetrical.

Longest Common Prefix: Finding commonality in paths (e.g., top.dut.bank0...).

Reverse Words in String: Reordering packet headers.

String to Integer (Atoi): Converting log strings to hex/decimal values.

Frequency Count: Count how many times each Error Code appears in a regression.

Anagram Check: Do two packets contain the same data in different orders?

Valid Parentheses: Check if your simulation "Begin/End" or "{ }" are balanced.

Group Anagrams: Group transactions by their data payload.

Pillar 4: The "Protocol Brain" (Logic & Algorithms)
Modeling how a chip actually makes decisions.

Implement a Stack (LIFO): Simulating a small return-address buffer.

Implement a Queue (FIFO): The most common hardware structure.

Linked List Cycle: Detecting if a pointer loop exists in memory.

Binary Search: Fastest way to find an address in a huge memory map.

Climbing Stairs: Simple recursion/DP (often asked to test logic flow).

Pascal’s Triangle: Generating coefficients for DSP/Filter verification.

Valid Sudoku: (Advanced) Testing constraint-based solvers.

First Unique Character: Identifying the first master to request the bus.

Find All Numbers Disappeared: Finding multiple dropped packets.

Matrix Transpose: Verifying data movement in an AI/NPU engine.

Pillar 5: The "Verification Architect" (Classes & OOP)
These test if you can write UVM-like Python (PyUVM).

Design a Scoreboard Class: Handle push_observed and push_expected.

Design a Circular Buffer: Implement write() and read() with wrap-around.

Inheritance Example: Create a BasePacket and a SecretPacket class.

Decorator for Logging: Write a function that automatically logs every time a method is called.

Singleton Pattern: Ensure only one ConfigDB exists for the testbench.

Generator Function: Use yield to create a stream of random transactions.

Try/Except/Finally: Writing robust code that doesn't crash if a log file is missing.

File I/O: Reading a CSV of register values and writing a Python Dictionary.

Lambda Functions: Sorting transactions by timestamp using a one-liner.

List Comprehension: Filtering all "Write" transactions from a list of "Read/Write".




#advanced

Pillar 6: The "System Architect" (Advanced Python)
These problems bridge the gap between "scripting" and "building a verification framework."

The "Producer-Consumer" Simulator (asyncio):

The Task: Use asyncio to simulate a Master (Producer) sending data to a FIFO and a Slave (Consumer) reading from it at different speeds.

Why: This mimics how Cocotb works. It tests your understanding of non-blocking code and "Simulated Time."

LRU Cache (Least Recently Used):

The Task: Implement an LRU Cache using an OrderedDict or a combination of a Dictionary and Double Linked List.

Why: This is a classic "Computer Architecture" interview question. It’s exactly how CPU caches decide which data to evict.

The "Big Log" Generator (Generators & Iterators):

The Task: Write a generator function yield that reads a 10GB log file line-by-line without loading the whole file into memory.

Why: A common "Senior" interview trap is asking you to parse a file larger than your RAM. If you use file.read(), you fail. You must use yield.

Deep vs. Shallow Copy Scoreboard:

The Task: Create a nested transaction object (a packet inside a frame). Show the difference between copy.copy() and copy.deepcopy() when adding it to a scoreboard.

Why: In UVM/Python, if you don't deep-copy transactions, your scoreboard will end up with "pointers" to the same object, corrupting your results.

DPI-C Wrapper (Type Hinting & ctypes):

The Task: Use the ctypes library to call a basic C function from Python.

Why: This is the Python equivalent of DPI-C. It proves you can interface with "Golden Models" written in C++.

Pillar 7: The "Regex Master" (Extreme Log Parsing)
Basic re.search isn't enough for Google/NVIDIA.

Multi-line Error Extraction:

The Task: In a log, an error starts with "ERROR: Code 0x..." and the details are on the next 3 lines. Use Regex to capture the code and the 3 lines of details together.

Why: Real hardware errors are rarely on a single line.

Clock Cycle Calculator:

The Task: Given a log where every line has a timestamp [10230 ns], calculate the delta (difference) between the first "Request" and the final "Acknowledgment" in clock cycles (assuming a 100MHz clock).

Pillar 8: "Cocotb" Style Coding
Since you know UVM, you should try the "Python version" of UVM.

Implement a "Monitor" Class: * Create a class that "observes" a list of transactions. It should have a Callback mechanism where it notifies a Scoreboard every time it sees a new valid packet.

Decorator for Coverage:

Write a Python Decorator @log_call that prints the arguments of a function every time it is called.

Why: This is how "Functional Coverage" is often implemented in Python-based verification environments.
