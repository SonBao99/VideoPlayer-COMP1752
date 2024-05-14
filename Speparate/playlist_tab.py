import tkinter as tk
from tkinter import ttk
import tkinter.scrolledtext as tkst
from base_tab import BaseTab

import tkinter as tk
from tkinter import ttk
from base_tab import BaseTab

class PlaylistTab(BaseTab):
    def __init__(self, notebook):
        super().__init__(notebook, 'Playlist')
        lbl_playlist = tk.Label(self.tab, text='Playlist')
        lbl_playlist.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.playlist_listbox = tk.Listbox(self.tab, width=55, height=10, selectmode=tk.SINGLE)
        self.playlist_listbox.grid(row=1, column=0, columnspan=2, rowspan=5, sticky="W", padx=10, pady=10)

        add_to_playlist_btn = tk.Button(self.tab, text="Add to Playlist", width=18)
        add_to_playlist_btn.grid(row=2, column=3, padx=10, pady=10)

        play_playlist_btn = tk.Button(self.tab, text="Play Playlist", width=18)
        play_playlist_btn.grid(row=3, column=3, padx=10, pady=10)

        remove_from_playlist_btn = tk.Button(self.tab, text="Remove from Playlist", width=18)
        remove_from_playlist_btn.grid(row=4, column=3, padx=10, pady=10)

        clear_playlist_btn = tk.Button(self.tab, text="Clear Playlist", width=18)
        clear_playlist_btn.grid(row=4, column=4, padx=10, pady=10)

        save_playlist_btn = tk.Button(self.tab, text="Save Playlist", width=18)
        save_playlist_btn.grid(row=2, column=4, padx=10, pady=10)

        load_playlist_btn = tk.Button(self.tab, text="Load Playlist", width=18)
        load_playlist_btn.grid(row=3, column=4, padx=10, pady=10)

        self.vid_num_frame = ttk.Frame(self.tab, borderwidth=5, relief='ridge')
        self.vid_num_frame.grid(row=1, column=3, columnspan=2, padx=10, pady=10)

        self.lbl_vid_num = tk.Label(self.vid_num_frame, text='Video Number')
        self.lbl_vid_num.grid(row=0, column=1, padx=10, pady=10)

        self.txt_vid_num = tk.Entry(self.vid_num_frame, width=10)
        self.txt_vid_num.grid(row=0, column=2, padx=10, pady=10, sticky='w')

        self.total_duration = 0

        self.total_duration_var = tk.StringVar()
        self.total_duration_label = tk.Label(self.tab, textvariable=self.total_duration_var, font=("Helvetica", 15), fg="blue")
        self.total_duration_label.grid(row=0, column=3, columnspan=3, padx=10, pady=10)

