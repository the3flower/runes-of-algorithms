def toggle_case(arr):
    output = []
    for char in arr:
        if 'A' <= char <= 'Z':  # Check if uppercase
            output.append(chr(ord(char) + 32))  # Convert to lowercase
        elif 'a' <= char <= 'z':  # Check if lowercase
            output.append(chr(ord(char) - 32))  # Convert to uppercase
        else:
            output.append(char)  # Keep unchanged if not a letter
    return output

# Example Test Cases
in_array1 = ['T', 'h', 'A', 'I', 'g', 'E', 'R', 'T', 'e', 'C']
in_array2 = ['I', 'a', 'M', 'a', 'g', 'O', 'D', 'o', 'F', 'S', 'o', 'F', 't', 'W', 'A', 'R', 'E']

print(toggle_case(in_array1))  # Expected: ['t', 'H', 'a', 'i', 'G', 'e', 'r', 't', 'E', 'c']
print(toggle_case(in_array2))  # Expected: ['i', 'A', 'm', 'A', 'G', 'o', 'd', 'O', 'f', 's', 'O', 'f', 'T', 'w', 'a', 'r', 'e']
