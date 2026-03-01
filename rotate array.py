from collections import deque

def rotate_like_hardware(nums, k):
    # 1. Convert list to a Queue (Shift Register)
    shift_reg = deque(nums)
    n = len(nums)
    k = k % n // it is just for how many time the array will rotate if 8%8=0 time roattion and 9%8= 1 time rotataion 
    
    # 2. Rotate k times
    for _ in range(k):
        # Remove from the 'Tail' and move to the 'Head'
        data_packet = shift_reg.pop()
        shift_reg.appendleft(data_packet)// Rotation Direction,Take From (Pop),Put To (Append),Python Function
                                         //Right →,pop() (Right),appendleft() (Left),d.rotate(1)//
                                          //Left ←,popleft() (Left),append() (Right),d.rotate(-1)//
        
    return list(shift_reg)

# Testbench
print(rotate_like_hardware([1, 2, 3, 4, 5], 2)) 
# Output: [4, 5, 1, 2, 3]
