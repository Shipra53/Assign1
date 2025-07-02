import streamlit as st
import os
from encryption import encrypt_file, decrypt_file
from config import Config
import io

# Set up the upload folder if it doesn't exist
if not os.path.exists(Config.UPLOAD_FOLDER):
    os.makedirs(Config.UPLOAD_FOLDER)

st.title(":blue[Secure File Sharing System]")

# Generate and save encryption key (this should ideally be securely stored)
key = Config.ENCRYPTION_KEY

# File Upload and Encryption
st.header("_Upload_ a File for :green[Encryption]",divider="violet")
uploaded_file = st.file_uploader("Choose a file to encrypt", type=["txt", "pdf", "jpg", "png"])

if uploaded_file is not None:
    # Read file data
    file_data = uploaded_file.read()
    encrypted_data = encrypt_file(file_data, key)
    filename = uploaded_file.name

    # Save encrypted file
    encrypted_filepath = os.path.join(Config.UPLOAD_FOLDER, filename)
    with open(encrypted_filepath, 'wb') as f:
        f.write(encrypted_data)

    st.success(f"File '{filename}' uploaded and encrypted successfully!")

# File Decryption and Download
st.header("Download a File")
if st.button("List Encrypted Files"):
    files = os.listdir(Config.UPLOAD_FOLDER)
    st.write("Encrypted Files Available for Download:")
    for file in files:
        st.write(file)

selected_file = st.text_input("Enter the name of the file to download:")

if selected_file:
    encrypted_filepath = os.path.join(Config.UPLOAD_FOLDER, selected_file)
    
    if os.path.exists(encrypted_filepath):
        with open(encrypted_filepath, 'rb') as f:
            encrypted_data = f.read()
        decrypted_data = decrypt_file(encrypted_data, key)

        # Provide decrypted file as download
        st.download_button(
            label="Download Decrypted File",
            data=io.BytesIO(decrypted_data),
            file_name=selected_file,
            mime="application/octet-stream"
        )
    else:
        st.error("File not found!")
