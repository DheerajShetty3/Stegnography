# Stegnography 

---

# 🔐 Secure Data Hiding in Images Using Steganography  

This project implements **steganography** to securely **hide and retrieve** secret messages inside images using Python, OpenCV, and NumPy.  

## 🛠️ Requirements  
Ensure you have the following installed:  
- Python 3.x  
- OpenCV (`cv2`)  
- NumPy  
- A `.png` image file (e.g., `gym.png`)  

Install dependencies using:  
```bash
pip install opencv-python numpy
```

## 🚀 How to Run the Code

### 1️⃣ Encrypt a Message into an Image 
1. Place `gym.png` in the same directory as the script.  
2. Run `encryption.py` (or the script containing the encryption code):  
   ```bash
   python e.py
   ```
3. Enter your secret message and a password when prompted.  
4. The encrypted image (`encryptedImage.png`) will be generated.  

### 2️⃣ Decrypt the Hidden Message 
1. Ensure `encryptedImage.png` and `password.txt` are present in the directory.  
2. Run `decryption.py` (or the script containing the decryption code):  
   ```bash
   python d.py
   ```
3. Enter the same password used for encryption.  
4. The hidden message will be revealed!  

## ⚠️ Notes  
- The password is required for decryption.  
- The image file must be in PNG format to avoid corruption.  
- If the message is too long, it may exceed the image’s capacity.  

## 📌 Use Cases  
✅ Secure Communication  
✅ Digital Watermarking  
✅ Cybersecurity & Data Protection  

---
