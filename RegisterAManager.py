from tkinter import *
import tkinter as tk

class RegisterAManager:
  def __init__(self, root, frame):
    self.root = root
    self.frame = frame

    self.registerA = tk.Label(self.frame, text="Register A", bg="#44505A", fg="white", font="timesnewroman").place(relx=0,rely=0)
    #self.registerB = tk.Label(self.frame, text="Register A", bg="#44505A", fg="white", font="timesnewroman").place(relx=0.34, rely=0)
    #elf.registerC = tk.Label(self.frame, text="Register C", bg="#44505A", fg="white", font="timesnewroman").place(relx=0.67, rely=0)

    #register A
    #nickels-----------------------------
    self.nickels = tk.DoubleVar()
    #self.nickels.trace_add("write", self.calculate)
    self.nickelEntry = tk.Entry(self.frame, textvariable=self.nickels, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.nickelEntry.place(relx=0, rely=0.035)
    self.nickelLab = tk.Label(self.frame, text="Nickels:", bg="#44505A", fg='white').place(relx=0.07, rely=0.035)
    self.nickelWorthLab = tk.Label(self.frame, text=self.nickels.get())
    self.nickelWorthLab.place(relx=0.14, rely=0.035)
    