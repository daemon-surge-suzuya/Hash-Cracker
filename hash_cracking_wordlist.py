import hashlib

def decode_hashes(hash_string):
    decoded_string = None
    #checking if the hash is MD5
    if len(hash_string) == 32:
        hash_type = 'md5'
    #checking if the hash is SHA1
    elif len(hash_string) == 40:
        hash_type = 'sha1'
    #checking if the hash is SHA256
    elif len(hash_string) == 64:
        hash_type = 'sha256'
    elif len(hash_string) == 56:
        hash_type = 'sha224'
    elif len(hash_string) == 96:
        hash_type = 'sha384'
    else:
        print("Unable to decode this type of Hash")
        return
    
    with open('wordlist.txt', 'r') as wordlist:
        for line in wordlist:
            word = line.strip()
            hashed_word = hashlib.new(hash_type, word.encode()).hexdigest()
            if hashed_word == hash_string:
                decoded_string = word
                break
    
    if decoded_string:
        print("Hash decrypted successfully: ", decoded_string)
    else:
        print("Could not decrypt the hash.")

decode_hashes(input("Your hash: "))

