import pickle
import os

KEYWORDS_FILE = "keywords.dat"
PASSWORDS_FILE = "passwords.dat"

keywords = []
passwords = []

def load_file(file):
    if os.path.exists(file):
        with open(file, "rb") as f:
            return pickle.load(f)
    return []

def save_file(file, data):
    with open(file, "wb") as f:
        pickle.dump(data, f)

def load_all():
    global keywords, passwords
    keywords[:] = load_file(KEYWORDS_FILE)
    passwords[:] = load_file(PASSWORDS_FILE)

def save_all():
    save_file(KEYWORDS_FILE, keywords)
    save_file(PASSWORDS_FILE, passwords)