def xor_string_with_127(input_string):
    result = ''
    for char in input_string:
        result += chr(ord(char) ^ 127)
    return result

input_string = "Hello World"
output_string = xor_string_with_127(input_string)
print(f"Original String: {input_string}")
print(f"String after XOR with 127: {output_string}")
