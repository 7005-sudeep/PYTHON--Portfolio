Pillar 1: The "Hardware Data" (Arrays & Lists)
These test your ability to handle streams of transaction data.

Move Zeros to End: (We did this!) Squeezing out bubbles in a pipeline.//complete

Two Sum: (We did this!) Checking address pairs. //complete

Majority Element: (We did this!) Arbiter/Voting logic. //complete

Missing Number: (We did this!) Dropped packet detection.

Contains Duplicate: (We did this!) Scoreboard collision check.

Best Time to Buy/Sell Stock: Finding max delta (latency/throughput analysis).

Rotate Array: Mimicking a circular buffer or barrel shifter.

Merge Sorted Arrays: Combining two sorted data streams (Arbiter logic).

Find the "Single" Number: Use XOR to find a non-repeated ID.

Intersection of Two Arrays: Finding common addresses in two memory maps.

Pillar 2: The "Bit-Smasher" (Bitwise Operations)
This is the #1 skill for ASIC engineers. Python handles bits differently than Verilog!

Count Set Bits: Calculate parity (Hamming weight).

Reverse Bits: Endianness conversion (Big-Endian to Little-Endian).

Power of Two: Check if an address is aligned to a power of 2.

Bitwise Swap: Swap two numbers without a temp variable using XOR.

Extract Bitfield: Given (val, high, low), extract specific bits.

Isolate Rightmost Set Bit: Common in priority encoders.

Gray Code to Binary: Converting sensor data or CDC pointers.

Find the Non-Repeating Bit: XOR magic with multiple numbers.

Check Parity: Return 1 if odd number of bits are set.

Set/Clear/Toggle a Bit: Basic register manipulation.

Pillar 3: The "Log Parser" (Strings & Files)
Verification engineers spend 50% of their time reading .log files.

Search for "ERROR": Scan a 1GB file and print lines containing "Fatal".

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
