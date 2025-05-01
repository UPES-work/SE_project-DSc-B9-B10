from user import user_menu
from admin import admin_menu

def main():
    while True:
        print("\n=== Movie Ticket Booking System ===")
        print("1. User")
        print("2. Admin")
        print("3. Exit")
        choice = input("Choose user type: ")

        if choice == '1':
            user_menu()
        elif choice == '2':
            admin_menu()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()