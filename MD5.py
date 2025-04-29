import hashlib

def calculate_md5(text):
    # Create an MD5 hash object
    md5_hash = hashlib.md5()
    
    # Update the object with the bytes of the input text
    md5_hash.update(text.encode('utf-8'))
    
    # Return the hexadecimal representation of the digest
    return md5_hash.hexdigest()

# Test the function with the string "Hello World"
input_string = "Hello World"
md5_result = calculate_md5(input_string)

print(f"Original String: {input_string}")
print(f"MD5 Hash: {md5_result}")
