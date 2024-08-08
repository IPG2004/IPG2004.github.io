import os
import json
import bcrypt
from face_recognition import capture_face, recognize_face

class Authentication:
    def __init__(self):
        self.DATA_FOLDER = 'data'
        if not os.path.exists(self.DATA_FOLDER):
            os.makedirs(self.DATA_FOLDER)

        # File to store the users
        self.USERS_FILE = os.path.join(self.DATA_FOLDER, 'users.json')

    # This function registers a new user.
    # It receives the username and password as parameters.
    # It returns True if the user was registered successfully, False otherwise.
    def register(self, username, password):
        # Load the existing users
        try:
            with open(self.USERS_FILE, 'r') as f:
                users = json.load(f)
        except FileNotFoundError:
            users = {}

        # Verify if the user already exists
        if username in users:
            return False

        # Create the hashed password
        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        # Save the new user
        users[username] = hashed
        with open(self.USERS_FILE, 'w') as f:
            json.dump(users, f)

        # Capture the face of the user
        capture_face(username)

        return True

    # This function logs in a user.
    # It receives the username and password as parameters.
    # It returns True if the user was logged in successfully, False otherwise.
    def login(self, username, password):
        # Load the existing users
        try:
            with open(self.USERS_FILE, 'r') as f:
                users = json.load(f)
        except FileNotFoundError:
            return False

        # Verify if the user exists
        if username not in users:
            return False

        # Verify the password
        hashed = users[username]
        if bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8')):
            # Verify the face
            if recognize_face(username):
                return True
        return False


# Test the Authentication class

# if __name__ == '__main__':
#     auth = Authentication()
#     auth.register('test', '1234')
#     auth.login('test', '1234')