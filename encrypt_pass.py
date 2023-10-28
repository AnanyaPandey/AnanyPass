import bcrypt

def hash_password(password):
    # Generate a random salt and hash the password
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    with open('user_password.pw', 'wb') as file:
        file.write(hashed_password)
    return 

def verify_password(password, stored_hash):
    # Check if the provided password matches the stored hash
    return bcrypt.checkpw(password.encode('utf-8'), stored_hash)