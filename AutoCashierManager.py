import tkinter as tk
from RegisterAManager import RegisterAManager
from RegisterBManager import RegisterBManager
from RegisterCManager import RegisterCManager
from CalculationManager import CalculationManager

class AutoCashierManager:
  def __init__(self):
    self.root = tk.Tk()
    self.root.title("AutoCashier")
    self.root.configure(background="#44505A")
    self.root.geometry("1000x700")

    # set up register A
    self.RegAFrame = tk.Frame(self.root, width=334, height=700, bg="green")
    self.RegAFrame.place(relx=0, rely=0)
    self.RegAPanel = RegisterAManager(self.root, self.RegAFrame)

    self.RegBFrame = tk.Frame(self.root, width=333, height=700, bg="yellow")
    self.RegBFrame.place(relx=0.34, rely=0)
    self.RegBPanel = RegisterBManager(self.root, self.RegBFrame)

    self.RegCFrame = tk.Frame(self.root, width=333, height=700, bg="red")
    self.RegCFrame.place(relx=0.67, rely=0)
    self.RegCPanel = RegisterCManager(self.root, self.RegCFrame)

    self.CalcManagerFrame = tk.Frame(self.root, width=1000, height=365, bg="blue")
    self.CalcManagerFrame.place(relx=0, rely=0.48)
    self.CalcManagerPanel = CalculationManager(self.root, self.CalcManagerFrame)

  def start(self):
    self.root.mainloop()