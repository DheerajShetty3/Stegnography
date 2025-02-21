import cv2
import numpy as np

# Load encrypted image
img = cv2.imread("encryptedImage.png", cv2.IMREAD_COLOR)

if img is None:
    print("Error: Encrypted image not found!")
    exit()

# Read stored password
try:
    with open("password.txt", "r") as f:
        stored_password = f.read().strip()
except FileNotFoundError:
    print("Error: Password file not found!")
    exit()

# Get password input
input_password = input("Enter the original passcode used for encryption: ")

if input_password != stored_password:
    print("Authentication failed!")
    exit()

# Get message length (from first pixel)
msg_length = img[0, 0, 0]

if msg_length == 0 or msg_length > (img.shape[0] * img.shape[1] * 3):
    print("Error: Invalid message length detected!")
    exit()

# Decrypt message
message = []
index = 0

for n in range(img.shape[0]):
    for m in range(img.shape[1]):
        for z in range(3):  # Iterate over R, G, B channels
            if index < msg_length:
                char_code = img[n, m, z]
                if 32 <= char_code <= 126:  # Only printable ASCII characters
                    message.append(chr(char_code))
                index += 1
            else:
                break  # Stop reading once message is fully extracted
        if index >= msg_length:
            break
    if index >= msg_length:
        break

print("Decrypted message:", "".join(message))
