import hashlib

def generate_rainbow_table(wordlist_file, hash_type):
    # Create the hash function based on the user input
    if hash_type == 'sha384':
        hash_function = hashlib.sha384
    elif hash_type == 'sha256':
        hash_function = hashlib.sha256
    elif hash_type == 'sha224':
        hash_function = hashlib.sha224
    elif hash_type == 'sha1':
        hash_function = hashlib.sha1
    elif hash_type == 'md5':
        hash_function = hashlib.md5
    else:
        print(f"Error: Invalid hash type: '{hash_type}'")
        return

    # Open the wordlist file
    with open(wordlist_file, 'r') as f:
        # Read the contents of the wordlist file
        words = f.readlines()

    # Create an empty list to store the rainbow table entries
    rainbow_table = []

    # Loop through each word in the wordlist
    for word in words:
        # Strip the newline character from the word
        word = word.strip()
        
        # Hash the word with the selected hash function
        hash_object = hash_function(word.encode())
        
        # Generate the hexadecimal representation of the hash
        hash_hex = hash_object.hexdigest()
        
        # Add the word and its hash to the rainbow table list
        rainbow_table.append(f'{word}:{hash_hex}')

    # Write the rainbow table to a new file
    with open(f'rainbow_table_{hash_type}.txt', 'w') as f:
        for entry in rainbow_table:
            f.write(entry + '\n')

hash_type = input("Enter the type of hash to use (sha384, sha256, sha224, sha1, or md5): ").lower()
wordlist_to_be_converted = input("Enter the name of the wordlist you want to convert: ")
generate_rainbow_table(wordlist_to_be_converted, hash_type)
