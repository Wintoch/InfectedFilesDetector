import customtkinter as ctk
from tkinter import filedialog
import pefile

ctk.set_appearance_mode("dark")

scanPath = ""

def extractFeatures():
    pass

def loadFile():
    global scanPath
    scanPath = filedialog.askopenfilename()

def scanFile():
    global scanPath
    if (scanPath == ""):
        labelReturn.configure(text="Error, you need to load the file")
    else:
        pe = pefile.PE(scanPath)

window = ctk.CTk()
window.title("Infected Files Detector")
window.geometry("500x400")

label = ctk.CTkLabel(window, text="When ready, click button below")
label.pack(pady=20)

button = ctk.CTkButton(window, text="Load file", command=loadFile, corner_radius=20)
button.pack(pady=10)

button = ctk.CTkButton(window, text="Scan", command=scanFile, corner_radius=20)
button.pack(pady=10)

labelReturn = ctk.CTkLabel(window, text="")
labelReturn.pack(pady=20)

window.mainloop()