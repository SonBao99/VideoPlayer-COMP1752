import tkinter as tk
from tkinter import messagebox as msb

import font_manager as fonts
import video_library as lib 

def set_text(text_area, content): #set text in a given text area
    text_area.delete("1.0", tk.END) #delete everything in the text area
    text_area.insert(1.0, content)  #insert the content

class UpdateVideo():
    def __init__(self, window):
        self.window = window
        self.window.geometry("600x200")
        self.window.title("Update Videos")

        self.__create_widgets()

    def __create_widgets(self):

        self.__lbl_vid_number = tk.Label(self.window, text="Enter Video Number")
        self.__lbl_vid_number.grid(row=1, column=0, padx=10, pady=10, sticky="W")

        self.__txt_vid_number = tk.Entry(self.window, width=3)
        self.__txt_vid_number.grid(row=1, column=1, padx=10, pady=10)

        self.__btn_check = tk.Button(self.window, text="Check", command=self.check_video_clicked)
        self.__btn_check.grid(row=1, column=2, padx=10, pady=10)

        self.__lbl_new_rating = tk.Label(self.window, text="Enter New Rating")
        self.__lbl_new_rating.grid(row=2, column=0, padx=10, pady=10, sticky="W")

        self.__txt_new_rating = tk.Entry(self.window, width=3)
        self.__txt_new_rating.grid(row=2, column=1, padx=10, pady=10)

        self.__btn_update = tk.Button(self.window, text="Update", command= self.update_video_clicked)
        self.__btn_update.grid(row=2, column=2,padx=10, pady=10)

        self.video_txt = tk.Text(self.window, width=24, height=4, wrap="none") 
        self.video_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)

        self.status_lbl = tk.Label(self.window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

    def check_video_clicked(self): #
        key = self.__txt_vid_number.get() #get the video number and assign it as 'key'
        name = lib.get_name(key) 
        if name is not None:
            director = lib.get_director(key)
            rating = lib.get_rating(key)
            play_count = lib.get_play_count(key)
            video_details = f"{name}\n{director}\nrating: {rating}\nplays: {play_count}"
            set_text(self.video_txt, video_details)
        else:
            msb.showerror("Error", "Video not found")

    def update_video_clicked(self):
    # Get the video number and new rating from the respective text entry widgets
        video_number = self.__txt_vid_number.get()
        new_rating = self.__txt_new_rating.get()

        # Validate video number
        if not video_number.isdigit() or int(video_number) <= 0:
            msb.showerror("Error", "Please enter a valid positive integer for the video number")
            return

        if not new_rating:
            msb.showerror("Error", "Please enter a new rating")
            return
        # Try to convert the new rating to an integer; show an error message if it's not a valid number
        try:
            new_rating = int(new_rating)
        except ValueError:
            msb.showerror("Error", "New rating must be a valid number")
            return

        # Check if both video number and new rating are provided
        if video_number and new_rating:
            # Get the current rating of the video from some library function (lib.get_rating)
            current_rating = lib.get_rating(video_number)

            # Check if the video with the given number exists
            if current_rating:
                # Check if the new rating is within the valid range (1 to 5)
                if  new_rating >=1 and new_rating <= 5:
                    # Update the rating of the video using some library function (lib.set_rating)
                    lib.set_rating(video_number, new_rating)
                    msb.showinfo("Success", "Video updated successfully!")
                else:
                    msb.showerror("Error", "Rating must be between 1 and 5")

                # Clear the text entry widgets and update a text widget (self.video_txt)
                self.__txt_vid_number.delete(0, tk.END)
                self.__txt_new_rating.delete(0, tk.END)
        
                self.video_txt.delete("1.0", tk.END)
            else:
                # Display a message if the video with the given number is not found
                set_text(self.video_txt, f"Video {video_number} not found")
        else:
            # Display an error message if either video number or new rating is missing
            msb.showerror("Error", "Please enter video number and new rating!")

if __name__ == "__main__":  # only runs when this file is run as a standalone
    window = tk.Tk()        # create a TK object
    fonts.configure()       # configure the fonts
    UpdateVideo(window)     
    window.mainloop()     