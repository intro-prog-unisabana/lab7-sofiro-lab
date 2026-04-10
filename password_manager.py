import csv

from caesar import caesar_encrypt


def encrypt_single_pass(filename: str) -> None:
    """TODO: Parte 1."""
    with open(filename, 'r') as file:
        password = file.read().strip()
    encrypted_password = caesar_encrypt(password)
    with open(filename, 'w') as file:
        file.write(encrypted_password)


def encrypt_passwords_in_file(filename: str) -> None:
    """Encripta las contraseñas en un archivo CSV."""
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        rows = [row for row in reader if row]
    for i in range(1, len(rows)): 
        password = rows[i][2]
        rows[i][2] = caesar_encrypt(password)
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)


def change_password(filename: str, website: str, password: str) -> bool:
    """TODO: Parte 3."""
    pass


def add_login(filename: str, website_name: str, username: str, password: str) -> None:
    """TODO: Parte 4."""
    pass
