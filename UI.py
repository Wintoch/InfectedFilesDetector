import customtkinter as ctk
from tkinter import filedialog

ctk.set_appearance_mode("dark")

def scanFile():
    print("Button works")

window = ctk.CTk()
window.title("Infected Files Detector")
window.geometry("500x400")

label = ctk.CTkLabel(window, text="When ready, click button below")
label.pack(pady=20)

button = ctk.CTkButton(window, text="Choose file and scan", command=scanFile, corner_radius=20)
button.pack(pady=10)

window.mainloop()