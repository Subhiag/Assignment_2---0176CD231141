students = {}
current_user = None

def register():
    print("----- Student Registration -----")
    username = input("Enter username: ").strip()
    if username in students:
        print("Username already exists. Try a different one.")
        return

    details = {
        "password": input("Enter password: "),
        "name": input("Enter full name: "),
        "age": input("Enter age: "),
        "gender": input("Enter gender: "),
        "email": input("Enter email: "),
        "phone": input("Enter phone number: "),
        "address": input("Enter address: "),
        "course": input("Enter course name: "),
        "year": input("Enter year of study: "),
        "college": input("Enter college name: ")
    }

    students[username] = details
    print(f"Registration successful! Welcome, {details['name']}.")

def login():
    global current_user
    print("--- Login ---")
    if current_user:
        print(f"Already logged in as {current_user}. Please logout first.")
        return
    username = input("Enter username: ").strip()
    password = input("Enter password: ")
    if username in students and students[username]["password"] == password:
        current_user = username
        print(f"Welcome back, {students[username]['name']}!")
    else:
        print("Invalid username or password.")

def show_profile():
    if not current_user:
        print("Please login first.")
        return
    print(f"--- Student Profile: {current_user} ---")
    for key, value in students[current_user].items():
        if key != "password":
            print(f"{key.capitalize()}: {value}")

def update_profile():
    if not current_user:
        print("Please login first.")
        return
    print("--- Update Profile ---")
    print("(Leave a field blank to keep it unchanged.)")
    user = students[current_user]
    updated = False
    for key in user:
        if key == "password":
            continue
        new_value = input(f"{key.capitalize()} ({user[key]}): ").strip()
        if new_value:
            user[key] = new_value
            updated = True
    if updated:
        print("Profile updated successfully!")
    else:
        print("No changes made.")

def change_password():
    if not current_user:
        print("Please login first.")
        return
    print("--- Change Password ---")
    user = students[current_user]
    old_password = input("Enter current password: ")
    if old_password != user["password"]:
        print("Incorrect password!")
        return
    new_password = input("Enter new password: ")
    confirm_password = input("Confirm new password: ")
    if new_password == confirm_password:
        user["password"] = new_password
        print("Password changed successfully!")
    else:
        print("Passwords do not match.")

def cancel_registration():
    global current_user
    if not current_user:
        print("Please login first.")
        return
    confirm = input("Are you sure you want to delete your account? (yes/no): ").lower()
    if confirm == "yes":
        del students[current_user]
        print("Account deleted successfully.")
        current_user = None
    else:
        print("Account deletion cancelled.")

def show_registered_users():
    print("--- Registered Users ---")
    if not students:
        print("No users registered yet.")
    else:
        for username in students:
            print(f"- {username} ({students[username]['name']})")

def logout():
    global current_user
    if current_user:
        print(f"Goodbye, {students[current_user]['name']}")
        current_user = None
    else:
        print("No user currently logged in.")

def terminate():
    global students, current_user
    confirm = input("Are you sure you want to TERMINATE the system? (yes/no): ").lower()
    if confirm == "yes":
        students.clear()
        current_user = None
        print("All data cleared. System terminated.")
        exit()
    else:
        print("Termination cancelled.")

def main():
    while True:
        print("----- Student Management System Menu -----")
        print("1. Register")
        print("2. Login")
        print("3. Show Profile")
        print("4. Update Profile")
        print("5. Logout")
        print("6. Change Password")
        print("7. Cancel Registration")
        print("8. Show Registered Users")
        print("9. Terminate System")
        choice = input("Enter your choice (1-9): ").strip()
        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            show_profile()
        elif choice == "4":
            update_profile()
        elif choice == "5":
            logout()
        elif choice == "6":
            change_password()
        elif choice == "7":
            cancel_registration()
        elif choice == "8":
            show_registered_users()
        elif choice == "9":
            terminate()
        else:
            print("Invalid choice! Please enter a number between 1 and 9.")

main()
