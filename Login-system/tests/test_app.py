import unittest
from app import App
import customtkinter as ctk

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = App()

    def test_initial_scaling(self):
        # Test initial scaling based on screen resolution
        screen_width = self.app.winfo_screenwidth()
        screen_height = self.app.winfo_screenheight()
        
        if screen_width < 1920 or screen_height < 1080:
            self.assertEqual(self.app.scaling, 1)
        elif screen_width < 2560 or screen_height < 1440:
            self.assertEqual(self.app.scaling, 1.5)
        else:
            self.assertEqual(self.app.scaling, 2)

    def test_change_appearance_mode(self):
        # Test changing the appearance mode
        self.app.change_appearance_mode("Light")
        self.assertEqual(ctk.get_appearance_mode(), "Light")
        
        self.app.change_appearance_mode("Dark")
        self.assertEqual(ctk.get_appearance_mode(), "Dark")

    def test_change_scaling(self):
        # Test changing the UI scaling
        self.app.change_scaling("1440p")
        self.assertEqual(self.app.scaling, 1.5)
        
        self.app.change_scaling("Manual")
        self.assertTrue(self.app.ui_button_minus.cget("state") == "enabled")
        self.assertTrue(self.app.ui_button_plus.cget("state") == "enabled")

    def test_modify_scaling(self):
        # Test manually modifying the UI scaling
        initial_scaling = self.app.scaling
        self.app.modify_scaling(1)
        self.assertEqual(self.app.scaling, initial_scaling + 0.1)
        
        self.app.modify_scaling(-1)
        self.assertEqual(self.app.scaling, initial_scaling)

if __name__ == "__main__":
    unittest.main()
