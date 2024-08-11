import unittest
import os
import sys

# Add the src directory to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.face_recognition import capture_face, recognize_face

class TestFaceRecognition(unittest.TestCase):

    def setUp(self):
        self.test_username = "test_user"
        self.data_folder = "data"
        self.user_folder = os.path.join(self.data_folder, self.test_username)
        
        # Create test user folder if it doesn't exist
        if not os.path.exists(self.user_folder):
            os.makedirs(self.user_folder)

    def tearDown(self):
        # Remove test user folder if it exists
        if os.path.exists(self.user_folder):
            for file in os.listdir(self.user_folder):
                os.remove(os.path.join(self.user_folder, file))
            os.rmdir(self.user_folder)

    def test_capture_face(self):
        # Test face capture
        capture_face(self.test_username)
        self.assertTrue(len(os.listdir(self.user_folder)) > 0)

    def test_recognize_face(self):
        # Test face recognition
        capture_face(self.test_username)
        self.assertTrue(recognize_face(self.test_username))

    def test_recognize_face_invalid_user(self):
        # Test face recognition with invalid user
        self.assertFalse(recognize_face("invalid_user"))

if __name__ == "__main__":
    unittest.main()
