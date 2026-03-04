from collections import deque

def rotate_circular_buffer(nums, k): # here think as fifo queae pop/append 
    # 1. Initialize the register
    register = deque(nums)
    n = len(nums)
    k = k % n  # Handle wrap-around logic
    
    # 2. Perform the shift k times
    for _ in range(k): # pop from end and append from start 
        # Hardware: Shift Right (MSB <--- LSB)
        data_packet = register.pop()      # Pop from the end
        register.appendleft(data_packet)  # Append to the front ## pop and append use at same time for data conversion and also for latency 
        
    return list(register)

# Testbench
bus_data = [1, 2, 3, 4, 5]
# After 2 rotations: [4, 5, 1, 2, 3]
print(f"Shifted Register: {rotate_circular_buffer(bus_data, 2)}")
