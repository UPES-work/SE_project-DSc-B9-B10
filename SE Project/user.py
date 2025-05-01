from utils import load_data, save_data
import uuid

def user_menu():
    while True:
        print("\n--- User Menu ---")
        print("1. View Movies and Showtimes")
        print("2. Book Ticket")
        print("3. Cancel Ticket")
        print("4. View My Bookings")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            view_movies()
        elif choice == '2':
            book_ticket()
        elif choice == '3':
            cancel_ticket()
        elif choice == '4':
            view_bookings()
        elif choice == '5':
            break
        else:
            print("Invalid choice.")

def view_movies():
    data = load_data()
    if not data['movies']:
        print("No movies available.")
        return
    for movie in data['movies']:
        print(f"Movie: {movie['title']}, Showtimes: {', '.join(movie['showtimes'])}")

def book_ticket():
    data = load_data()
    view_movies()
    movie_title = input("Enter movie title to book: ")
    showtime = input("Enter preferred showtime: ")
    seat = input("Enter seat number: ")

    booking_id = str(uuid.uuid4())[:8]
    booking = {
        "booking_id": booking_id,
        "movie": movie_title,
        "showtime": showtime,
        "seat": seat
    }

    data['bookings'].append(booking)
    save_data(data)
    print(f"Booking confirmed. Your Booking ID is {booking_id}")

def cancel_ticket():
    data = load_data()
    bid = input("Enter Booking ID to cancel: ")
    original_len = len(data['bookings'])
    data['bookings'] = [b for b in data['bookings'] if b['booking_id'] != bid]
    save_data(data)
    if len(data['bookings']) < original_len:
        print("Booking cancelled.")
    else:
        print("Booking ID not found.")

def view_bookings():
    data = load_data()
    if not data['bookings']:
        print("No bookings yet.")
        return
    for b in data['bookings']:
        print(f"ID: {b['booking_id']}, Movie: {b['movie']}, Time: {b['showtime']}, Seat: {b['seat']}")