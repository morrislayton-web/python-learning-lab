# Formatting user data for a database
first_name = input("Enter first name: ").strip().capitalize()
last_name = input("Enter last name: ").strip().capitalize()
email = input("Enter email: ").strip().lower()

username = f"{first_name[0]}{last_name}".lower()

print(f"--- User Created ---")
print(f"Full Name: {first_name} {last_name}")
print(f"System Username: {username}")
print(f"Verified Email: {email}")
