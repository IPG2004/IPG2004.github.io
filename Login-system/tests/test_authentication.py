import unittest
import os
import json
from src.authentication import Authentication

class TestAuthentication(unittest.TestCase):

    def setUp(self):
        self.auth = Authentication()
        self.test_username = "test_user"
        self.test_password = "test_pass"
        
        # Remove test data file if it exists
        if os.path.exists(self.auth.USERS_FILE):
            os.remove(self.auth.USERS_FILE)

    def tearDown(self):
        # Remove test data file if it exists
        if os.path.exists(self.auth.USERS_FILE):
            os.remove(self.auth.USERS_FILE)

    def test_register(self):
        # Test user registration
        self.assertTrue(self.auth.register(self.test_username, self.test_password))
        
        with open(self.auth.USERS_FILE, 'r') as f:
            users = json.load(f)
        
        self.assertIn(self.test_username, users)

    def test_register_existing_user(self):
        # Test registering an existing user
        self.auth.register(self.test_username, self.test_password)
        self.assertFalse(self.auth.register(self.test_username, self.test_password))

    def test_login(self):
        # Test user login
        self.auth.register(self.test_username, self.test_password)
        self.assertTrue(self.auth.login(self.test_username, self.test_password))

    def test_login_invalid_credentials(self):
        # Test login with invalid credentials
        self.auth.register(self.test_username, self.test_password)
        self.assertFalse(self.auth.login(self.test_username, "wrong_pass"))

    def test_login_non_existing_user(self):
        # Test login with a non-existing user
        self.assertFalse(self.auth.login(self.test_username, self.test_password))

if __name__ == "__main__":
    unittest.main()
