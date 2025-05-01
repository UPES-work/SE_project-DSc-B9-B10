# 🎬 Movie Ticket Booking System

## 📖 Project Overview

This is a basic **console-based Movie Ticket Booking System** developed in Python. It allows users to view available movies, select showtimes, book seats, and cancel bookings—all through a text-based interface. It is an offline system using a simple text file as a database, designed for single-user use without internet connectivity.

---

## 📦 Dependencies

This project requires only the Python Standard Library:

- `json`
- `os`
- `uuid`

✅ No third-party packages are required.

---

## ▶️ How to Run the Project

1. **Install Python** (version 3.x recommended):  
   Download from [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. **Extract the ZIP folder**:
   - Unzip `movie_ticket_booking.zip` to your local machine.

3. **Navigate to the project directory**:
   ```bash
   cd movie_ticket_booking
   ```

4. **Run the program**:
   ```bash
   python main.py
   ```

---

## 🛠 Technologies Used

- **Programming Language:** Python 3
- **Database:** File-based (`database.txt` using JSON format)
- **Interface:** Console-based Text UI

---

## ❓ Problem Statement

Booking movie tickets often involves long queues or complicated apps. This system provides a **simple, offline alternative** to book movie tickets quickly and easily through a terminal interface.

---

## ✨ Key Features

- View available movies and showtimes
- Book tickets with seat selection
- Cancel bookings using Booking ID
- Admin panel for managing movies and showtimes
- Persistent storage in a text file

---

## 🎯 Target Audience

- Students learning Python and software development
- Small-scale cinema owners who want a lightweight, offline booking tool
- Educational institutions for demo or project submissions

---

## 🔁 SDLC Model Followed

We adopted the **Waterfall Model** for this project due to its structured approach and clarity of phases:
1. Requirement Gathering
2. Design
3. Implementation
4. Testing
5. Deployment
6. Maintenance

---

## 📋 Requirements Gathering Approach

- Requirements were derived from everyday use cases of systems like BookMyShow.
- Brainstormed ideas within the group to define functional and non-functional needs.
- Validated by peer reviews and feedback from friends after initial prototypes.

---

## 🧪 Testing Approach

- **Manual Testing** was conducted by executing various scenarios:
  - Valid and invalid bookings
  - Admin actions like add/update/remove movies
  - Handling of incorrect inputs and empty datasets
- Positive and negative test cases were used to validate reliability.

---

## ⚠️ Development Challenges

| Challenge | Solution |
|----------|----------|
| Data persistence without DB | Used JSON with a `.txt` file to mimic DB functionality |
| Simple seat management | Used basic string entry for seat number |
| Admin authentication | Implemented basic password-based login |
| Avoiding crashes from empty data | Default fallback data added in file operations |

---

## 🚀 Deployment Instructions

No deployment necessary—this is a **local, offline system**. Just run `main.py` using Python on your local machine.

---

## 🌱 Future Enhancements

- Add GUI using Tkinter or PyQt
- Integrate seat layout and real-time seat blocking
- Enable online payments
- Expand to multi-user support
- Convert to a web application using Flask/Django

---

## 👥 Team Members and Roles

| Name            | SAP ID      | Role                        |
|-----------------|-------------|-----------------------------|
| Garvit Gupta    | 500124123   | Python Developer, UI logic |
| Harsh Vardhan   | 500122468   | Requirement Analyst, Tester|
| Vansh Chauhan   | 500121920   | Database & Admin logic     |
| **Supervisor**  | Ms. Richa Kumari | Academic Guide         |

---

## 📬 Feedback

We received feedback from peers suggesting the system was easy to use. A few mentioned a reminder feature would enhance user experience, which we plan to add in the next version.

---