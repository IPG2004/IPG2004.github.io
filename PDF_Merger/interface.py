import customtkinter as ctk
from tkinter import filedialog


ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):

  ui_button_plus = None
  ui_button_minus = None
  wres = ["1080p", "1440p", "4K", "Manual"]
  scaling = None
  content = []
  scrollframe = None
  footer_destination = None
  destination= None
  footer_name = None

  def __init__(self):
    super().__init__()
    self.title("PDF Merger")
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
      self.geometry("3720x1960")
      self.wres[0], self.wres[2] = self.wres[2], self.wres[0]
      ctk.set_widget_scaling(float(2))
      self.scaling = 2

    # configure grid layout (4x4)
    self.grid_columnconfigure(1, weight=1)
    self.grid_rowconfigure(0, weight=1)
    

    # create sidebar frame with widgets
    self.sidebar_frame = ctk.CTkFrame(self, width=140, corner_radius=0)
    self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
    self.sidebar_frame.grid_rowconfigure(1, weight=1)
    self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="PDF Merger", font=ctk.CTkFont(size=20, weight="bold"))
    self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

    # self.color_theme = ctk.CTkLabel(self.sidebar_frame, text="Color Theme:", anchor="w")
    # self.color_theme.grid(row=2, column=0, padx=20, pady=(10, 0))
    # self.color_theme_optionemenu = ctk.CTkOptionMenu(self.sidebar_frame, values=["Blue", "Green", "Dark Blue"],
    #                                                                    command=self.change_color_theme)
    # self.color_theme_optionemenu.grid(row=3, column=0, padx=20, pady=(10, 10))

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

    self.frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
    self.frame.grid(row=0, column=1, sticky="nsew")
    self.frame.grid_columnconfigure(0, weight=1)
    self.frame.grid_rowconfigure(0, weight=1)
    self.frame_content = ctk.CTkFrame(self.frame, corner_radius=0, fg_color="transparent")
    self.frame_content.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
    
    

    self.credit = ctk.CTkLabel(self.frame, text="Made by @IPG2004", font=ctk.CTkFont(size=20, weight="bold"))
    self.credit.grid(row=1, column=0, sticky="nsew", padx=0, pady=0, ipadx=20, ipady=20)


    self.frame_content.grid_columnconfigure(0, weight=1)
    self.frame_content.grid_rowconfigure(1, weight=1)

    frame_header = ctk.CTkFrame(self.frame_content, corner_radius=20)
    frame_header.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
    frame_header.grid_columnconfigure(0, weight=1)
    header_clear = ctk.CTkButton(frame_header, text="Clear", command=self.clear_scfr)
    header_clear.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
    header_search = ctk.CTkButton(frame_header, text="Search", command=self.select_file)
    header_search.grid(row=0, column=2, sticky="nsew", padx=10, pady=10, ipadx=10, ipady=10)

    self.scrollframe = ctk.CTkScrollableFrame(self.frame_content, corner_radius=20)
    self.scrollframe.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
    self.scrollframe.grid_columnconfigure(0, weight=1)
    self.build_scrollframe()
    
    frame_footer = ctk.CTkFrame(self.frame_content, corner_radius=20)
    frame_footer.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)
    frame_footer.grid_columnconfigure(0, weight=1)

    self.footer_destination = ctk.CTkLabel(frame_footer, text="Destination folder", corner_radius=20)
    self.footer_destination.grid(row=0, column=0, sticky="nsw", padx=10, pady=10)
    footer_destination_search = ctk.CTkButton(frame_footer, text="Destination", command=self.select_destination_folder)
    footer_destination_search.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
    self.footer_name = ctk.CTkEntry(frame_footer, corner_radius=20, placeholder_text="Filename")
    self.footer_name.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
    footer_merge = ctk.CTkButton(frame_footer, text="Merge", command=self.merge)
    footer_merge.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)




  # def change_color_theme(self, theme: str):
  #   if theme == "Blue":
  #     theme = "blue"
  #   elif theme == "Green":
  #     theme = "green"
  #   elif theme == "Dark Blue":
  #     theme = "dark-blue"
  #   ctk.set_default_color_theme(theme)


  def change_appearance_mode(self, mode):
    ctk.set_appearance_mode(mode)

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
    elif new_scaling == "4k":
      self.geometry("3840x2160")
      ctk.set_widget_scaling(float(2))
      self.scaling = 2
      
    
  def modify_scaling(self, value: int):
    if (value > 0):
      self.scaling += 0.1
    else:
      self.scaling -= 0.1
    ctk.set_widget_scaling(self.scaling)

  def remove_scfr(self, index):
    self.content.pop(index)
    self.scrollframe.destroy()
    self.scrollframe = ctk.CTkScrollableFrame(self.frame_content, corner_radius=20)
    self.scrollframe.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
    self.scrollframe.grid_columnconfigure(0, weight=1)
    self.build_scrollframe()

  def clear_scfr(self):
    self.content = []
    self.scrollframe.destroy()
    self.scrollframe = ctk.CTkScrollableFrame(self.frame_content, corner_radius=20)
    self.scrollframe.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
    self.scrollframe.grid_columnconfigure(0, weight=1)
    self.footer_destination.configure(text="Destination folder", fg_color="transparent")
    self.footer_name.delete(0, "end")
    self.footer_name.configure(placeholder_text="Filename", fg_color=("#F9F9FA", "#343638"))
    

  def build_scrollframe(self):
    i = 1
    for files in self.content:
      new_frame = ctk.CTkFrame(self.scrollframe, corner_radius=20)
      new_frame.grid_columnconfigure(1, weight=1)
      ctk.CTkLabel(new_frame, text=f"{i}").grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
      ctk.CTkLabel(new_frame, text=files).grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
      ctk.CTkButton(new_frame, text="Remove", command=lambda e=i:self.remove_scfr(e-1)).grid(row=0, column=2, sticky="nsew", padx=10, pady=10)
      new_frame.grid(row=i-1, column=0, sticky="nsew", padx=10, pady=10)
      i += 1
      
  
  def add_content(self):
    for i in range(20):
      new_frame = ctk.CTkFrame(self.scrollframe, corner_radius=20)
      new_frame.grid_columnconfigure(1, weight=1)
      ctk.CTkLabel(new_frame, text=f"{i+1}").grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
      ctk.CTkLabel(new_frame, text=f"Filepath/filename{i+1}.pdf").grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
      ctk.CTkButton(new_frame, text="Remove", command=lambda e=i:self.remove_scfr(e)).grid(row=0, column=2, sticky="nsew", padx=10, pady=10)
      new_frame.grid(row=i, column=0, sticky="nsew", padx=10, pady=10)
      self.content.append(f"Filepath/filename{i}.pdf")
    


  def select_file(self):
    file = filedialog.askopenfilename(title="Select a file", filetypes=[("PDF files", "*.pdf")])
    if file:
      self.content.append(file)
      self.scrollframe.configure(fg_color="transparent")
      self.build_scrollframe()


  def select_destination_folder(self):
    folder = filedialog.askdirectory(title="Select a folder")
    if folder:
      self.footer_destination.configure(text=folder, fg_color="transparent")

  
  def merge(self):
    error = False
    if self.content == []:
      self.scrollframe.configure(fg_color="red")
      error = True
    if self.footer_destination.cget("text") == "Destination folder":
      self.footer_destination.configure(fg_color="red")
      error = True
    if self.footer_name.get() == "":
      self.footer_name.configure(fg_color="red")
      error = True
    if error:
      return
    if self.footer_name.get()[-4:] != ".pdf":
      self.footer_name.insert("end", ".pdf")
    try:
      from PyPDF2 import PdfMerger
      merger = PdfMerger()
      for file in self.content:
        merger.append(file)
      merger.write(f"{self.footer_destination.cget('text')}/{self.footer_name.get()}")
      merger.close()
    except Exception:
      error = ctk.CTkToplevel(self)
      error.title("Error")
      error.grid_columnconfigure(0, weight=1)
      error.grid_rowconfigure(0, weight=1)
      error_label = ctk.CTkLabel(error, text="An error occured while merging the files.", font=ctk.CTkFont(size=20, weight="bold"))
      error_label.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
      close_button = ctk.CTkButton(error, text="Close", command=lambda:(error.destroy(), self.clear_scfr()))
      close_button.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
      return
    
