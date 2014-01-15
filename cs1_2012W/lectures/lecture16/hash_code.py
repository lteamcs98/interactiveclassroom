def my_hash_function(key):
    assert type(key) == str  # check if the key is a string
    
    hash_code = 0
    for char in key:
        hash_code += ord(char)    

    return hash_code

print my_hash_function("pat")
print my_hash_function("let")

print hash("banana")