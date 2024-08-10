import customtkinter as ctk
from src.authentication import Authentication

# Pre-configure the appearance mode and color theme
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("green")

class App(ctk.CTk):

  # Declare all the widgets and variables
  ui_button_plus = None
  ui_button_minus = None
  wres = ["1080p", "1440p", "4K", "Manual"]
  scaling = None
  frame_content = None
  auth = Authentication()
  
  # Initialize the application
  def __init__(self):
    super().__init__()
    self.title("Authentication System")
    # Set the window size based on the screen resolution
    if (self.winfo_screenwidth() < 1920) or (self.winfo_screenheight() < 1080):
      self.geometry("1820x980")
      ctk.set_widget_scaling(float(1))
      self.scaling = 1
    elif (self.winfo_screenwidth() < 2560) or (self.winfo_screenheight() < 1440):
      self.geometry("2420x1340")
      self.wres[0], self.wres[1] = self.wres[1], self.wres[0]
      ctk.set_widget_scaling(float(1.5))
      self.scaling = 1.5
    else:
      self.geometry("3740x2060")
      self.wres[0], self.wres[2] = self.wres[2], self.wres[0]
      ctk.set_widget_scaling(float(2))
      self.scaling = 2

    # Configure the grid layout
    self.grid_columnconfigure(1, weight=1)
    self.grid_rowconfigure(0, weight=1)
    
    # create sidebar frame with widgets
    self.sidebar_frame = ctk.CTkFrame(self, width=140, corner_radius=0)
    self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
    self.sidebar_frame.grid_rowconfigure(1, weight=1)
    self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="Login\nSystem", font=ctk.CTkFont(size=20, weight="bold"))
    self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

    self.appearance_mode_label = ctk.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
    self.appearance_mode_label.grid(row=4, column=0, padx=20, pady=(10, 0))
    self.appearance_mode_optionemenu = ctk.CTkOptionMenu(self.sidebar_frame, values=["System", "Light", "Dark"],
                                                                       command=self.change_appearance_mode)
    self.appearance_mode_optionemenu.grid(row=5, column=0, padx=20, pady=(10, 10))
    self.scaling_label = ctk.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
    self.scaling_label.grid(row=6, column=0, padx=20, pady=(10, 0))
    self.scaling_optionemenu = ctk.CTkOptionMenu(self.sidebar_frame, values=self.wres,
                                                               command=self.change_scaling)
    self.scaling_optionemenu.grid(row=7, column=0, padx=20, pady=(10, 20))
    self.ui_button_frame = ctk.CTkFrame(self.sidebar_frame, fg_color="transparent")
    self.ui_button_frame.grid(row=8, column=0)
    self.ui_button_frame.grid_columnconfigure((0,1), weight=1)
    self.ui_button_minus = ctk.CTkButton(self.ui_button_frame, state="disabled", text="-", command=lambda:self.modify_scaling(-1), width=70, corner_radius=0)
    self.ui_button_minus.grid(row=0, column=0, padx=(20,0), pady=10)
    self.ui_button_plus = ctk.CTkButton(self.ui_button_frame, state="disabled", text="+", command=lambda:self.modify_scaling(1), width=70, corner_radius=0)
    self.ui_button_plus.grid(row=0, column=1, padx=(0,20), pady=10)

    # create main frame with widgets
    self.frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
    self.frame.grid(row=0, column=1, sticky="nsew")
    self.frame.grid_columnconfigure(0, weight=1)
    self.frame.grid_rowconfigure(0, weight=1)
    self.frame_content = ctk.CTkFrame(self.frame, corner_radius=0, fg_color="transparent")
    self.frame_content.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
    
    

    self.credit = ctk.CTkLabel(self.frame, text="Made by @IPG2004", font=ctk.CTkFont(size=20, weight="bold"))
    self.credit.grid(row=1, column=0, sticky="nsew", padx=0, pady=0, ipadx=20, ipady=20)

    self.create_widgets()
    

  # functions to change the appearance mode
  def change_appearance_mode(self, mode):
    ctk.set_appearance_mode(mode)

  # functions to change the scaling
  def change_scaling(self, new_scaling: str):
    if new_scaling == "Manual":
      self.ui_button_minus.configure(state="enabled")
      self.ui_button_plus.configure(state="enabled")
    else:
      self.ui_button_minus.configure(state="disabled")
      self.ui_button_plus.configure(state="disabled")

    if new_scaling == "1080p":
      self.geometry("1920x1080")
      ctk.set_widget_scaling(float(1))
      self.scaling = 1
    elif new_scaling == "1440p":
      self.geometry("2560x1440")
      ctk.set_widget_scaling(float(1.5))
      self.scaling = 1.5
    elif new_scaling == "4K":
      self.geometry("3740x2060")
      ctk.set_widget_scaling(float(2))
      self.scaling = 2
      
  # function to modify manually the scaling
  def modify_scaling(self, value: int):
    if (value > 0):
      self.scaling += 0.1
    else:
      self.scaling -= 0.1
    ctk.set_widget_scaling(self.scaling)

  # function to create the initial widgets
  def create_widgets(self):
    self.frame_content.destroy()
    self.frame_content = ctk.CTkFrame(self.frame, corner_radius=0, fg_color="transparent")
    self.frame_content.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
    self.frame_content.grid_columnconfigure(0, weight=1)
    self.frame_content.grid_rowconfigure((0,3), weight=1)

    login_button = ctk.CTkButton(self.frame_content, text="Login", width=200, height=40, font=ctk.CTkFont("Arial", 20), command=self.build_login)
    login_button.grid(row=1, column=0, padx=20, pady=20)
    register_button = ctk.CTkButton(self.frame_content, text="Register", width=200, height=40, font=ctk.CTkFont("Arial", 20), command=self.build_register)
    register_button.grid(row=2, column=0, padx=20, pady=20)

  # function to build the login widgets
  def build_login(self):
    self.frame_content.destroy()
    self.frame_content = ctk.CTkFrame(self.frame, corner_radius=0, fg_color="transparent")
    self.frame_content.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
    self.frame_content.grid_columnconfigure(0, weight=1)
    self.frame_content.grid_rowconfigure((0,7), weight=1)

    user_label = ctk.CTkLabel(self.frame_content, text="User", font=ctk.CTkFont("Arial", size=20, weight="bold"))
    user_label.grid(row=1, column=0, padx=20, pady=10)
    user_entry = ctk.CTkEntry(self.frame_content, width=200, height=40, font=ctk.CTkFont("Arial", 20))
    user_entry.grid(row=2, column=0, padx=20, pady=10)

    password_label = ctk.CTkLabel(self.frame_content, text="Password", font=ctk.CTkFont("Arial", size=20, weight="bold"))
    password_label.grid(row=3, column=0, padx=20, pady=10)
    password_entry = ctk.CTkEntry(self.frame_content, show="*", width=200, height=40, font=ctk.CTkFont("Arial", 20))
    password_entry.grid(row=4, column=0, padx=20, pady=10)

    login_button = ctk.CTkButton(self.frame_content, text="Login", width=200, height=40, font=ctk.CTkFont("Arial", 20), command=lambda: self.login(user_entry.get(), password_entry.get()))
    login_button.grid(row=5, column=0, padx=20, pady=20)

    back_button = ctk.CTkButton(self.frame_content, text="Back", width=200, height=40, font=ctk.CTkFont("Arial", 20), command=self.create_widgets)
    back_button.grid(row=6, column=0, padx=20, pady=20)

  # function to build the register widgets
  def build_register(self):
    self.frame_content.destroy()
    self.frame_content = ctk.CTkFrame(self.frame, corner_radius=0, fg_color="transparent")
    self.frame_content.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
    self.frame_content.grid_columnconfigure(0, weight=1)
    self.frame_content.grid_rowconfigure((0,7), weight=1)

    user_label = ctk.CTkLabel(self.frame_content, text="User", font=ctk.CTkFont("Arial", size=20, weight="bold"))
    user_label.grid(row=1, column=0, padx=20, pady=10)
    user_entry = ctk.CTkEntry(self.frame_content, width=200, height=40, font=ctk.CTkFont("Arial", 20))
    user_entry.grid(row=2, column=0, padx=20, pady=10)

    password_label = ctk.CTkLabel(self.frame_content, text="Password", font=ctk.CTkFont("Arial", size=20, weight="bold"))
    password_label.grid(row=3, column=0, padx=20, pady=10)
    password_entry = ctk.CTkEntry(self.frame_content, show="*", width=200, height=40, font=ctk.CTkFont("Arial", 20))
    password_entry.grid(row=4, column=0, padx=20, pady=10)

    register_button = ctk.CTkButton(self.frame_content, text="Register", width=200, height=40, font=ctk.CTkFont("Arial", 20), command=lambda: self.register(user_entry.get(), password_entry.get()))
    register_button.grid(row=5, column=0, padx=20, pady=20)

    back_button = ctk.CTkButton(self.frame_content, text="Back", width=200, height=40, font=ctk.CTkFont("Arial", 20), command=self.create_widgets)
    back_button.grid(row=6, column=0, padx=20, pady=20)

  # function to register a new user
  def register(self, username, password):
    if self.auth.register(username, password):
      # Show the success message
      self.frame_content.destroy()
      self.frame_content = ctk.CTkFrame(self.frame, corner_radius=0, fg_color="transparent")
      self.frame_content.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
      self.frame_content.grid_columnconfigure(0, weight=1)
      self.frame_content.grid_rowconfigure((0,3), weight=1)
      register_label = ctk.CTkLabel(self.frame_content, text=f"User {username} registered successfully", font=ctk.CTkFont("Arial", size=20, weight="bold"))
      register_label.grid(row=1, column=0, padx=20, pady=20)
      back_button = ctk.CTkButton(self.frame_content, text="Back", width=200, height=40, font=ctk.CTkFont("Arial", 20), command=self.create_widgets)
      back_button.grid(row=2, column=0, padx=20, pady=20)
    else:
      # Show a popup with the error message
      popup = ctk.CTkToplevel(self)
      popup.title("Error")
      popup.geometry("600x400")
      popup_label = ctk.CTkLabel(popup, text="User already exists", font=ctk.CTkFont("Arial", size=20, weight="bold"))
      popup_label.pack(padx=20, pady=20)
      popup_button = ctk.CTkButton(popup, text="Close", width=200, height=40, font=ctk.CTkFont("Arial", 20), command=popup.destroy)
      popup_button.pack(padx=20, pady=20)
  
  # function to login a user
  def login(self, username, password):
    if self.auth.login(username, password):
      # Show the welcome message
      self.frame_content.destroy()
      self.frame_content = ctk.CTkFrame(self.frame, corner_radius=0, fg_color="transparent")
      self.frame_content.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
      self.frame_content.grid_columnconfigure(0, weight=1)
      self.frame_content.grid_rowconfigure((0,3), weight=1)
      login_label = ctk.CTkLabel(self.frame_content, text=f"Welcome back, {username}", font=ctk.CTkFont("Arial", size=20, weight="bold"))
      login_label.grid(row=1, column=0, padx=20, pady=20)
      back_button = ctk.CTkButton(self.frame_content, text="Back", width=200, height=40, font=ctk.CTkFont("Arial", 20), command=self.create_widgets)
      back_button.grid(row=2, column=0, padx=20, pady=20)
    else:
      # Show a popup with the error message
      popup = ctk.CTkToplevel(self)
      popup.title("Error")
      popup.geometry("600x400")
      popup_label = ctk.CTkLabel(popup, text="Invalid credentials", font=ctk.CTkFont("Arial", size=20, weight="bold"))
      popup_label.pack(padx=20, pady=20)
      popup_button = ctk.CTkButton(popup, text="Close", width=200, height=40, font=ctk.CTkFont("Arial", 20), command=popup.destroy)
      popup_button.pack(padx=20, pady=20)

# Run the application
if __name__ == "__main__":
    app = App()
    app.mainloop()