import tkinter as tk
import font_manager as fonts
from PIL import Image, ImageTk 
import os
from video_player import VideoPlayer
import video_library as lib


class CreateVideoList():
    def __init__(self, window):
        self.window = window
        self.window.geometry('860x750')
        self.window.title('Create Video List')

        self.video_list = []  # List to store video numbers

        self.back_btn = tk.Button(self.window, text="Back",command=self.back_btn_clicked)
        self.back_btn.grid(row=0, column=1, padx=10, pady=10, sticky='w')



        # Upper - Video List
        self.lbl_list = tk.Label(self.window, text='Video List')
        self.lbl_list.grid(row=1, column=1, padx=10, pady=10, columnspan=3)

        self.video_listbox = tk.Listbox(self.window, width=55, height=10, selectmode=tk.SINGLE)
        self.video_listbox.grid(row=2, column=1, columnspan=3, rowspan=5, sticky="W", padx=10, pady=10)
        self.video_listbox.bind("<<ListboxSelect>>", self.video_item_selected)

        # Lower - Playlist
        self.lbl_playlist = tk.Label(self.window, text='Playlist')
        self.lbl_playlist.grid(row=7, column=1, columnspan=2, padx=10, pady=10)

        self.playlist_listbox = tk.Listbox(self.window, width=55, height=10, selectmode=tk.SINGLE)
        self.playlist_listbox.grid(row=8, column=1, columnspan=2, rowspan=5, sticky="W", padx=10, pady=10)
        self.playlist_listbox.bind("<<ListboxSelect>>", self.playlist_item_selected)

        # Right side - Video Entry and Buttons
        self.lbl_vid_num = tk.Label(self.window, text='Video Number')
        self.lbl_vid_num.grid(row=2, column=4, padx=10, pady=10)

        self.txt_vid_num = tk.Entry(self.window, width=3)
        self.txt_vid_num.grid(row=3, column=4, padx=10, pady=10)

        self.add_to_playlist_btn = tk.Button(self.window, text="Add to Playlist",width=18, command=self.add_to_playlist)
        self.add_to_playlist_btn.grid(row=4, column=4, padx=10, pady=10)

        self.play_playlist_btn = tk.Button(self.window, text="Play Playlist", width=18, command=self.play_playlist)
        self.play_playlist_btn.grid(row=8, column=4, padx=10, pady=10)

        self.remove_from_playlist_btn = tk.Button(self.window, text="Remove from Playlist", width=18, command=self.remove_from_playlist)
        self.remove_from_playlist_btn.grid(row=9, column=4, padx=10, pady=10)

        self.clear_playlist_btn = tk.Button(self.window, text="Clear Playlist",width=18, command=self.clear_playlist)
        self.clear_playlist_btn.grid(row=10, column=4, padx=10, pady=10)


        self.video_cover_label = tk.Label(self.window, text='Video Cover')
        self.video_cover_label.grid(row=0, column=5, padx=10, pady=10, rowspan=5)

        # Display cover picture
        self.cover_image = tk.Label(self.window)
        self.cover_image.grid(row=1, column=4, rowspan=5, padx=10, pady=10)

        # Call the method to update the video cover when a video is selected
        self.video_item_selected(None)

        self.list_videos_clicked()  # Automatically load the video list when the window is opened
    def back_btn_clicked(self):
        VideoPlayer(tk.Toplevel(window))
    def video_item_selected(self, event):
        selected_index = self.video_listbox.curselection()
        if selected_index:
            selected_video_number = self.video_list[selected_index[0]]
            self.display_cover_picture(selected_video_number)
        else:
            print("No video selected")
    
    def display_cover_picture(self, video_number):
        # Fetch the cover picture file path from the video_library module
        cover_picture_path = lib.get_cover_picture(video_number)

        # Load the cover picture using Pillow
        img = Image.open(cover_picture_path)
        img = img.resize((150, 200), Image.ANTIALIAS)  # Adjust the size as needed
        img = ImageTk.PhotoImage(img)

        # Update the image on the GUI
        self.cover_image.config(image=img)
        self.cover_image.image = img

    def update_video_cover(self, video_number):
        # Assuming you have a function to get the file path of the cover image
        cover_image_path = lib.get_cover_image_path(str(video_number))

        if cover_image_path:
            # Open the image file using Pillow
            image = Image.open(cover_image_path)
            # Resize the image if needed
            image = image.resize((150, 200), Image.ANTIALIAS)
            # Convert the image to Tkinter PhotoImage format
            photo = ImageTk.PhotoImage(image)

            # Update the label with the new image
            self.video_cover_label.config(image=photo)
            self.video_cover_label.image = photo
        else:
            # If cover image is not found, you can display a default image or handle it accordingly
            default_image = tk.PhotoImage(width=150, height=200)
            self.video_cover_label.config(image=default_image)
            self.video_cover_label.image = default_image

    @staticmethod
    def get_cover_image_path(video_number):
        cover_filename = f"{video_number}.jpg"

        if os.path.exists(cover_filename):
            return cover_filename
        else:
            # If the cover image is not found, you can return None or a default image path
            return None
    def remove_from_playlist(self):
        pass
    def play_playlist(self):
        pass


    def add_to_playlist(self):
    # Check if the video is selected from the video listbox
        selected_index = self.video_listbox.curselection()
        if selected_index:
            video_number = self.video_list[selected_index[0]]
            print(f"Selected Video Number from listbox: {video_number}")
            video_name = lib.get_name(str(video_number))
            print(f"Video Name from listbox: {video_name}")
            if video_name is not None:
                self.txt_vid_num.delete(0, tk.END)
                self.txt_vid_num.insert(tk.END, str(video_number))
                self.update_playlist_text()
            else:
                print("Video not found in get_name for listbox")
        else:
            print("No video selected from the listbox")

            # If no video is selected from the video listbox, use the video number from the entry field
            video_number = self.txt_vid_num.get()
            if video_number:
                print(f"Video Number from entry field: {video_number}")
                video_name = lib.get_name(str(video_number))
                print(f"Video Name from entry field: {video_name}")
                if video_name is not None:
                    current_playlist = self.playlist_listbox.get(0, tk.END)  # Get all lines in the listbox
                    new_entry = f"{video_name}\n"
                    updated_playlist = current_playlist + (new_entry,)
                    self.playlist_listbox.delete(0, tk.END)  # Delete all lines in the listbox
                    self.playlist_listbox.insert(tk.END, *updated_playlist)  # Insert updated content
                else:
                    print("Video not found in get_name for entry field")
            else:
                print("No video selected from the entry field")


    def update_playlist_text(self):
        current_playlist = self.playlist_listbox.get(0, tk.END)
        video_number = self.video_list[-1]
        video_name = lib.get_name(str(self.video_list[-1]))  # Convert video_number to a string
        video_director = lib.get_director(str(self.video_list[-1]))
        self.playlist_listbox.insert(tk.END, f'{video_number} - {video_name} - {video_director}')

        

    def clear_playlist(self):
        self.video_list = []  # Clear the list
        self.video_listbox.delete(0, tk.END)
        self.playlist_listbox.delete(0, tk.END)
        

    def list_videos_clicked(self):
        # Instead of calling lib.list_all(), we'll use the keys from the library dictionary
        video_list = lib.list_all()
        self.video_listbox.delete(0, tk.END)
        self.video_list = list(video_list)  # Update the video list
        for video_number in video_list:
            video_name = lib.get_name(str(video_number))  # Convert video_number to a string
            video_director = lib.get_director(str(video_number))
            video_rating = lib.get_rating(str(video_number))
            star_rating = self.rating_to_stars(video_rating)
            self.video_listbox.insert(tk.END, f'{video_number} - {video_name} - {video_director} - Rating: {star_rating}')  # Add video_name)

    def video_item_selected(self, event):
        selected_index = self.video_listbox.curselection()
        if selected_index:
            selected_item = self.video_listbox.get(selected_index[0])
            print(f"Selected Video: {selected_item}")
        else:
            print("No video selected")

    def playlist_item_selected(self, event):
        selected_index = self.playlist_listbox.curselection()
        if selected_index:
            selected_item = self.playlist_listbox.get(selected_index[0])
            print(f"Selected Item: {selected_item}")
        else:
            print("No item selected")
    
    def rating_to_stars(self, rating):
        if rating is not None:
            return "★" * int(rating)
        return ""

if __name__ == "__main__":
    window = tk.Tk()
    fonts.configure()
    CreateVideoList(window)
    window.mainloop()
