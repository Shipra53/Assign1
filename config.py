import os

class Config:
    UPLOAD_FOLDER = 'uploads/'
    ENCRYPTION_KEY = os.urandom(32)  # Generate a secure key for encryption
