from password_manager import add_login, change_password, encrypt_passwords_in_file


def main() -> None:
    """Programa principal interactivo."""
    
    filename = input("Enter the CSV file name:\n")
    encrypt_passwords_in_file(filename)

    while True:
        print("Options: (1) Change Password, (2) Add Password, (3) Quit:")
        option = input()

        if option == "1":
            user_input = input("Enter the website and the new password:\n")
            parts = user_input.split()

            if len(parts) < 2:
                print("Input is in the wrong format!")
                continue

            website, new_password = parts[0], parts[1]

            if len(new_password) < 12:
                print("Password is too short!")
                continue

            success = change_password(filename, website, new_password)

            if not success:
                print("Website not found! Operation failed.")
            else:
                print("Password changed.")

        elif option == "2":
            user_input = input("Enter the website, username, and password:\n")
            parts = user_input.split()

            if len(parts) < 3:
                print("Input is in the wrong format!")
                continue

            website, username, password = parts[0], parts[1], parts[2]

            if len(password) < 12:
                print("Password is too short!")
                continue

            add_login(filename, website, username, password)
            print("Login added.")
        
        elif option == "3":
            break

        else:
            print("Invalid option selected!")


if __name__ == "__main__":
    main()