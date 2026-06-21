contacts = [
    {"name": "Aman", "phone": "1111111111", "email": "aman@gmail.com"},
    {"name": "Riya", "phone": "2222222222", "email": "riya@gmail.com"},
    {"name": "Karan", "phone": "3333333333", "email": "karan@gmail.com"},
    {"name": "Neha", "phone": "4444444444", "email": "neha@gmail.com"},
    {"name": "Rahul", "phone": "5555555555", "email": "rahul@gmail.com"}
]

def find_contact(name):
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            return contact
    return "Contact not found"

search = input("Enter name: ")
print(find_contact(search))
