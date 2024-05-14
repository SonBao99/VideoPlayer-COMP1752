# reviews_tab.py

import tkinter as tk
from tkinter import ttk
import tkinter.scrolledtext as tkst
from tkinter import messagebox as msb
import video_library as lib

class ReviewsTab:
    def __init__(self, notebook):
        self.create_review_tab(notebook)

    def create_review_tab(self, notebook):
        # REVIEW TAB
        reviews_frame = ttk.Frame(notebook)
        notebook.add(reviews_frame, text='Reviews', padding=5)

        # REVIEW WIDGETS
        self.lbl_review = tk.Label(reviews_frame, text='Reviews')
        self.lbl_review.grid(row=0, column=0, columnspan=3, padx=10, pady=10,)

        self.video_review_list = tkst.ScrolledText(reviews_frame, width=67, height=12, wrap="word")
        self.video_review_list.grid(row=1, column=0, columnspan=3, rowspan=4, padx=10, pady=10, sticky='nsew')

        self.lbl_new_review = tk.Label(reviews_frame, text="Enter Review")
        self.lbl_new_review.grid(row=2, column=4, padx=10, pady=10, sticky="W")

        self.__txt_new_review = tkst.ScrolledText(reviews_frame, width=30, height=10, wrap="none")
        self.__txt_new_review.grid(row=2, column=5, padx=10, pady=10, sticky="W")

        self.__lbl_new_rating = tk.Label(reviews_frame, text="Select New Rating")
        self.__lbl_new_rating.grid(row=1, column=4, padx=10, pady=10, sticky="W")

        ratings = [1, 2, 3, 4, 5]
        self.__selected_rating = tk.StringVar(value=ratings[0])
        self.__rating_dropdown = ttk.Combobox(reviews_frame, textvariable=self.__selected_rating, values=ratings, state="readonly", width=6)
        self.__rating_dropdown.grid(row=1, column=5, padx=10, pady=10, sticky="W")

        self.__btn_update = tk.Button(reviews_frame, text="Rate", command=self.rate_video_clicked)
        self.__btn_update.grid(row=1, column=5, padx=10, pady=10)

    def rate_video_clicked(self):
        # ... (same as in the original code)
        selected_index = self.video_listbox.curselection()

        if selected_index:
            video_number = self.video_list[selected_index[0]]
            new_rating = int(self.__rating_dropdown.get())
            new_rating_stars = "★" * new_rating

            if lib.get_rating(video_number):
                lib.set_rating(video_number, new_rating)
                new_review = self.__txt_new_review.get("1.0", tk.END)
                # Add the new review to the list of reviews only if it's not empty
                if new_review != "":
                    lib.add_review(video_number, new_review)

                msb.showinfo("Success", "Video rated successfully!")

                # Update the video_review_list widget with all reviews for the selected video
                self.update_video_reviews(video_number)
                
                # Update video list when press the rate button
                updated_item = self.video_listbox.get(selected_index[0])
                video_name = lib.get_name(str(video_number))
                video_director = lib.get_director(str(video_number))
                updated_item = f'{video_number} - {video_name} - {video_director} - Rating: {new_rating_stars}'  # Assuming the format is "video_number - Rating: current_rating"
                self.video_listbox.delete(selected_index[0])
                self.video_listbox.insert(selected_index[0], updated_item)

                self.__txt_new_review.delete("1.0", tk.END)
            else:
                msb.showerror("Error", f"Video {video_number} not found")
        else:
            msb.showerror("Error", "Please select a video!")

# Add any additional functions or modifications if needed.
