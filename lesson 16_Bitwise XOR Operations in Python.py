# Lesson 16: Bitwise XOR Operations in Python
# Practicing
# Date: 2025-07-09

x = 9   # binary 1001
y = 5 # binary 0101
z = x ^ y # bitwise XOR operation; result in binary: 1100, in decimal: 12
print(f"z = {z}")   # z = 12
print(f"z = {z:0b}")    # z = 1100


x = 45  # binary 101101 (number to encrypt)
key = 102   # binary 1100110 (key)
encrypt = x ^ key # encryption
print(f"Encrypted number: {encrypt}")
decrypt = encrypt ^ key # decryption; Encryption result will be 75, decryption will return 45
print(f"Decrypted number: {decrypt}")


x = 9   # binary 1001
y = 5   # binary 0101
x = x ^ y
y = x ^ y
x = x ^ y
# now x = 5, y = 9 values are swapped
print(f"x = {x}")   # x = 5
print(f"y = {y}")   # y = 9