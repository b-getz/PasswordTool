import zxcvbn
import secrets
import string

def test_password_strength():
    password = input ("Enter the password to test: ")
    results = zxcvbn.zxcvbn(password)
    print("\nPassword Strength Results: ")
    print(f"Score: {results['score']} (0=Weak, 4=Strong)")
    print("Feedback: ")
    for suggestion in results['feedback']['suggestions']:
        print(f"- {suggestion}")
        if results['feedback']['warning']:
            print(f"- {results['feedback']['warning']}")
        else:
            print("- None")

def generate_password():
    length = 20

    char_set = string.ascii_letters + string.digits + string.punctuation

    # Generate Password
    password = ''.join(secrets.choice(char_set) for _ in range(length))
    print(f"\Generated Secure Password: {password}")

def show_menu():
    print("Password Tool Menu")
    print("1. Test Password Strength")
    print("2. Generate a Secure Password")
    print("3. Exit")

def main():
    while True:
        show_menu()
        choice = input("Enter Your Choice (1-3): ")
        if choice == '1':
            test_password_strength()
        elif choice == '2':
            generate_password()
        elif choice == '3':
            print("Exiting Program...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
