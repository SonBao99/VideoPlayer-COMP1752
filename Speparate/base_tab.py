import tkinter as tk
from tkinter import ttk

class BaseTab:
    def __init__(self, notebook, text):
        self.tab = ttk.Frame(notebook)
        notebook.add(self.tab, text=text, padding=5)

if __name__ == "__main__":
    window = tk.Tk()

    notebook = ttk.Notebook(window)
    BaseTab(notebook, text='Tab 1')
    window.mainloop()