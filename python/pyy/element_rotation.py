from icecream import ic
ic.disable


def rotate_left(arr, positions):
    # Calculate the effective rotation amount
    rotations = positions % len(arr) 
    ic(positions)
    ic(len(arr))
    ic(rotations)
        
    # Perform rotation
    rotated = arr[rotations:] + arr[:rotations]
    ic(arr[rotations:]) # [start : end ]
    ic(arr[:rotations])
    
    return rotated

# Example usage
arr = [1, 2, 3, 4, 5]
positions = 2

result = rotate_left(arr, positions)
print()
print("Original array:", arr)
print("Rotated array:", result)
print()
