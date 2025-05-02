from utils import load_data, save_data

ADMIN_PASSWORD = "admin123"

def admin_menu():
    pwd = input("Enter admin password: ")
    if pwd != ADMIN_PASSWORD:
        print("Incorrect password.")
        return

    while True:
        print("\n--- Admin Menu ---")
        print("1. Add Movie")
        print("2. Remove Movie")
        print("3. Update Showtimes")
        print("4. View Movies")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_movie()
        elif choice == '2':
            remove_movie()
        elif choice == '3':
            update_showtimes()
        elif choice == '4':
            view_movies()
        elif choice == '5':
            break
        else:
            print("Invalid choice.")

def add_movie():
    data = load_data()
    title = input("Enter movie title: ")
    showtimes = input("Enter showtimes (comma separated): ").split(',')
    data['movies'].append({"title": title.strip(), "showtimes": [s.strip() for s in showtimes]})
    save_data(data)
    print("Movie added.")

def remove_movie():
    data = load_data()
    title = input("Enter movie title to remove: ")
    data['movies'] = [m for m in data['movies'] if m['title'] != title]
    save_data(data)
    print("Movie removed if it existed.")

def update_showtimes():
    data = load_data()
    title = input("Enter movie title to update: ")
    for movie in data['movies']:
        if movie['title'] == title:
            new_times = input("Enter new showtimes (comma separated): ").split(',')
            movie['showtimes'] = [t.strip() for t in new_times]
            save_data(data)
            print("Showtimes updated.")
            return
    print("Movie not found.")

def view_movies():
    data = load_data()
    for movie in data['movies']:
        print(f"Movie: {movie['title']}, Showtimes: {', '.join(movie['showtimes'])}")