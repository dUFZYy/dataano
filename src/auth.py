import getpass
import hashlib
import os
import sys

SECRET_FILE = ".secret"

def hash_password(password: str) -> str:
    """Returns the SHA-256 hash of the given password."""
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def setup_password():
    """Prompts the user to set up a new password."""
    print("No password set. Let's set up your access.")
    pwd = getpass.getpass("Enter new password: ")
    pwd2 = getpass.getpass("Confirm password: ")
    
    if pwd == pwd2:
        with open(SECRET_FILE, "w") as f:
            f.write(hash_password(pwd))
        print("Password set successfully.\n")
    else:
        print("Passwords do not match. Exiting.")
        sys.exit(1)

def authenticate():
    """Authenticates the user before allowing access."""
    if not os.path.exists(SECRET_FILE):
        setup_password()
    
    try:
        with open(SECRET_FILE, "r") as f:
            stored_hash = f.read().strip()
    except Exception:
        print("Failed to read the secret file. Exiting.")
        sys.exit(1)
        
    pwd = getpass.getpass("Enter password to access TaskManager Pro: ")
    if hash_password(pwd) != stored_hash:
        print("Access denied.")
        sys.exit(1)
