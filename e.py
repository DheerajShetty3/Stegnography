import cv2
import os
import numpy as np

# Load image
img = cv2.imread("gym.png", cv2.IMREAD_COLOR)  # Ensure this file exists

if img is None:
    print("Error: Image not found!")
    exit()

# Get input message and password
msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

# Store password for decryption
with open("password.txt", "w") as f:
    f.write(password)

# Ensure message length does not exceed image capacity
max_capacity = (img.shape[0] * img.shape[1] * 3) - 1  # Minus 1 for length storage
if len(msg) > max_capacity:
    print("Error: Message is too long for this image!")
    exit()

# Encrypt message length in the first pixel (0,0)
img[0, 0, 0] = len(msg)  # Store message length in the blue channel

# Encrypt the message
index = 0
for n in range(img.shape[0]):
    for m in range(img.shape[1]):
        for z in range(3):  # Iterate over R, G, B channels
            if index < len(msg):
                img[n, m, z] = ord(msg[index])  # Store ASCII value
                index += 1
            else:
                break  # Stop once message is fully stored
        if index >= len(msg):
            break
    if index >= len(msg):
        break

# Save encrypted image as PNG to prevent corruption
cv2.imwrite("encryptedImage.png", img)
os.system("start encryptedImage.png")  # Open the image on Windows

print("Message encrypted successfully!")
