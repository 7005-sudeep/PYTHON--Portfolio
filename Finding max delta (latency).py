# differnce between max-min 

def find_max_performance_delta(data_points):
    # Initialize 'min_val' to infinity so any first number is smaller
    min_val = float('inf') 
    max_delta = 0
    
    for current_val in data_points:
        # 1. Update the 'Lowest Point' seen so far
        if current_val < min_val:
            min_val = current_val
            
        # 2. Calculate potential delta (current - lowest)
        current_delta = current_val - min_val
        
        # 3. Update 'Global Max Delta' if this one is better
        if current_delta > max_delta:
            max_delta = current_delta
            
    return max_delta

# --- AXI4 Simulation Trace (Latency in nanoseconds) ---
latency_trace = [7, 1, 5, 3, 6, 4]
# Lowest latency was 1ns, followed by a peak of 6ns. 
# Max Delta = 5ns.

print(f"Maximum Throughput Delta: {find_max_performance_delta(latency_trace)}")




# another way in this we assume min latency and max gap to 0 

def get_max_latency_delta(trace):
    # We start by assuming the first point is the minimum
    min_latency = trace[0]
    max_gap = 0
    
    for current_latency in trace:
        # Update the lowest point seen so far
        if current_latency < min_latency:
            min_latency = current_latency
        
        # Calculate the jump from the lowest point to here
        current_gap = current_latency - min_latency
        
        # If this jump is bigger than our previous record, save it
        if current_gap > max_gap:
            max_gap = current_gap
            
    return max_gap

# Simulation Data: Latency in cycles
axi_trace = [10, 2, 8, 1, 6, 9] 
# Note: Even though 10 is high, it's at the start. 
# The best delta is from 1 to 9 = 8.
print(f"Peak Performance Delta: {get_max_latency_delta(axi_trace)} cycles")
