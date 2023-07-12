import hashlib

def decode_hashes(hash_string):
    decoded_string = None
    #checking if the hash is MD5
    if len(hash_string) == 32:
        hash_type = 'md5'
        rainbow_table_file = 'rainbow_stable_md5.txt'
    #checking if the hash is SHA1
    elif len(hash_string) == 40:
        hash_type = 'sha1'
        rainbow_table_file = 'rainbow_table_sha1.txt'
    #checking if the hash is SHA256
    elif len(hash_string) == 64:
        hash_type = 'sha256'
        rainbow_table_file = 'rainbow_table_sha256.txt'
    elif len(hash_string) == 56:
        hash_type = 'sha224'
        rainbow_table_file = 'rainbow_table_sha224.txt' 
    elif len(hash_string) == 96:
        hash_type = 'sha384'
        rainbow_table_file = 'rainbow_table_sha384.txt'
    else:
        print("Unable to decode this type of Hash")
        return
    
    with open(rainbow_table_file, 'r') as rainbow_table:
        for line in rainbow_table:
            word, word_hash = line.strip().split(':')
            if word_hash == hash_string:
                decoded_string = word
                break
    
    if decoded_string:
        print("Hash decrypted successfully: ", decoded_string)
    else:
        print("Could not decrypt the hash.")

decode_hashes(input("Your hash: "))
