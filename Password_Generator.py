import random
import string

def generate_password(length):
    
    characters = string.ascii_letters + string.digits + string.punctuation
    
    if length < 1:
        print("Password length must be at least 1")
    
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    length = int(input("Enter the desired length of the password: "))
    password = generate_password(length)
    if password != "":
        print("Generated Password: ", password)

if __name__ == "__main__":
    main()
