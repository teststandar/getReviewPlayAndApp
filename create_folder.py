import os

def create_folder(name):
    os.makedirs(name, exist_ok=True)

def clear_screen():
    # Untuk Windows
    if os.name == 'nt':
        os.system('cls')
    # Untuk macOS/Linux
    else:
        os.system('clear')