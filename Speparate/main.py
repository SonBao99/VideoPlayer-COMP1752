import tkinter as tk
from tkinter import ttk
from base_tab import BaseTab
from review_tab import ReviewTab
from playlist_tab import PlaylistTab

if __name__ == "__main__":
    window = tk.Tk()

    notebook = ttk.Notebook(window)
    ReviewTab(notebook)
    PlaylistTab(notebook)

    window.mainloop()