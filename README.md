# Secure File Sharing System

A Secure File Sharing System built in Python that allows users to upload, encrypt, and share files securely. This application provides end-to-end encryption for file storage, protecting sensitive data and enabling safe sharing.

## Table of Contents
- Features
- Tech Stack
- Folder Structure
- Getting Started
    - Prerequisites
    - Installation
    - Usage
- How It Works
- Future Enhancements
- Contributing

## Features
#### File Encryption: 
- Automatically encrypt files upon upload, ensuring confidentiality.

#### Secure Storage: 
- Files are stored in encrypted form, preventing unauthorized access.

#### Decryption and Download: 
- Authorized users can decrypt and download files securely.

#### User Interface: 
- Built with Streamlit for a simple and interactive experience.

## Tech Stack
#### Python: 
Core language for backend functionality.

#### Cryptography: 
Library used to encrypt and decrypt files securely.

#### Streamlit: 
Used to create an interactive and intuitive web-based user interface.

#### Flask/Django (Optional): 
Can be added to extend backend functionality if needed.

## Folder Structure
```bash
Secure-File-Sharing-System/
│
├── app.py              # Main Streamlit app for the file sharing interface
├── config.py           # Configuration file with encryption key and upload path
├── encryption.py       # Script containing encryption and decryption functions
├── uploads/            # Directory for storing encrypted files
└── README.md           # Project documentation and setup guide
```

## Getting Started
#### Prerequisites
Python 3.8+

#### Required libraries: 
cryptography, streamlit

#### Installation
Clone the Repository

```bash
Copy code
git clone https://github.com/your-username/Secure-File-Sharing-System.git
cd Secure-File-Sharing-System
```
#### Install Dependencies

Install required Python libraries.

```bash
Copy code
pip install -r requirements.txt
```
#### Set Up the Upload Directory
Ensure the uploads/ directory is present for storing encrypted files:

```bash
mkdir -p uploads
```
#### Configure Encryption Key
Add your encryption key in config.py for secure storage and retrieval.

##  Usage
#### Run the Application
- Start the Streamlit application.

```bash
Copy code
streamlit run app.py
```
#### Encrypt and Upload a File
- Go to the upload section and select a file. The file will be encrypted and stored securely.

#### Download and Decrypt a File
- To retrieve a file, enter the filename and download the decrypted content.

## How It Works
- Encryption: Files are encrypted using a symmetric encryption key, ensuring that data is secure during storage.
- Decryption: Only users with the correct key can decrypt and access the original file.
- User Interface: Streamlit provides an interactive and easy-to-use interface for managing files.

## Future Enhancements
- User Authentication: Adding secure user login functionality.
- Key Management: Integrate a secure key management system.
- File Expiration: Auto-delete files after a specified time to increase security.

## Contributing
Contributions are welcome! Please open issues or submit pull requests for any enhancements or fixes.
