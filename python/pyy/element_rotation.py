def rotate_left(arr, positions):
    # Calculate the effective rotation amount
    rotations = positions % len(arr)
    
    # Perform rotation
    rotated = arr[rotations:] + arr[:rotations]
    
    return rotated

# Example usage
arr = [1, 2, 3, 4, 5]
positions = 2
result = rotate_left(arr, positions)
print()
print("Original array:", arr)
print("Rotated array:", result)
print()
