#######################################################################################################################################################


#THIS SCRIPT IS MADE BY DAEMON_SURGE_SUZUYA
#THIS SCRIPT IS SINGLE THREADED MEANS THAT IT WILL WORK FASTER FOR SHORT PASSWORDS BUT IT WON'T USE ALL OF YOUR CPU CORES TO DECODE PASSWORDS.
#BUT YOU CAN MODIFY THIS CODE USING MULTI-PROCESS SO THAT IT CAN CRACK PASSWORDS WITH THE USE OF ALL OF YOUR CPU CORES 


#######################################################################################################################################################
import hashlib
import itertools

# Get the hash to crack
hash_to_crack = input("Enter the hash to crack: ")

# Determine what type of hash it is 
hash_type = None 
if len(hash_to_crack) == 32:  # MD5 hashes are 32 characters long 
    hash_type = "md5" 
elif len(hash_to_crack) == 40: # SHA1 hashes are 40 characters long 
    hash_type = "sha1" 
elif len(hash_to_crack) == 64: # SHA256 hashes are 64 characters long 
    hash_type = "sha256" 
else:
    print("Unsupported Hash Type")

# If the length matches any of the supported types, then proceed with cracking
if hash_type:
    # Generate all possible combinations of lowercase letters, uppercase letters, and numbers
    charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

for length in range(1, 11):
    for attempt in itertools.product(charset, repeat=length):
        attempt_str = ''.join(attempt)
        attempt_bytes = attempt_str.encode('utf-8')
        if hash_type == "md5":
            attempt_hash = hashlib.md5(attempt_bytes).hexdigest()
        elif hash_type == "sha1":
            attempt_hash = hashlib.sha1(attempt_bytes).hexdigest()
        elif hash_type == "sha256":
            attempt_hash = hashlib.sha256(attempt_bytes).hexdigest()
        if attempt_hash == hash_to_crack:
            print("Hash cracked! The password is {}".format(attempt_str))
            break
    else:
        continue
    break

