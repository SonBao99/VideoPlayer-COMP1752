import tkinter as tk
from tkinter import ttk
import tkinter.scrolledtext as tkst
from base_tab import BaseTab

class ReviewTab(BaseTab):
    def __init__(self, notebook):
        super().__init__(notebook, 'Reviews')

        # REVIEW WIDGETS
        self.lbl_review = tk.Label(self.tab, text='Reviews')
        self.lbl_review.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        self.video_review_list = tkst.ScrolledText(self.tab, width=67, height=12, wrap="word")
        self.video_review_list.grid(row=1, column=0, columnspan=3, rowspan=4, padx=10, pady=10, sticky='nsew')

        self.lbl_new_review = tk.Label(self.tab, text="Enter Review")
        self.lbl_new_review.grid(row=2, column=4, padx=10, pady=10, sticky="W")

        self.__txt_new_review = tkst.ScrolledText(self.tab, width=30, height=10, wrap="none")
        self.__txt_new_review.grid(row=2, column=5, padx=10, pady=10, sticky="W")

        self.__lbl_new_rating = tk.Label(self.tab, text="Select New Rating")
        self.__lbl_new_rating.grid(row=1, column=4, padx=10, pady=10, sticky="W")

        ratings = [1, 2, 3, 4, 5]
        self.__selected_rating = tk.StringVar(value=ratings[0])
        self.__rating_dropdown = ttk.Combobox(self.tab, textvariable=self.__selected_rating, values=ratings, state="readonly", width=6)
        self.__rating_dropdown.grid(row=1, column=5, padx=10, pady=10, sticky="W")

        self.__btn_update = tk.Button(self.tab, text="Rate", command=self.rate_video_clicked)
        self.__btn_update.grid(row=1, column=5, padx=10, pady=10)

    def rate_video_clicked(self):
        # Implement rating functionality
        pass