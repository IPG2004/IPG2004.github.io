import unittest
import sys
import os

# Add the src directory to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

# from app import App

class TestYouTubeDownloader(unittest.TestCase):
    
    def test_app_initialization(self):
        app = App()
        self.assertIsNotNone(app)

    def setUp(self):
        self.app = App()

    def test_change_appearance_mode(self):
        self.app.change_appearance_mode("Light")
        self.assertEqual(ctk.get_appearance_mode(), "Light")

    def test_change_scaling(self):
        self.app.change_scaling("1080p")
        self.assertEqual(self.app.scaling, 1)
        self.app.change_scaling("1440p")
        self.assertEqual(self.app.scaling, 1.5)
        self.app.change_scaling("4k")
        self.assertEqual(self.app.scaling, 2)

    def test_clear_scfr(self):
        self.app.url_entry.insert(0, "Test URL")
        self.app.clear_scfr()
        self.assertEqual(self.app.url_entry.get(), "")

if __name__ == "__main__":
    unittest.main()
