import tkinter as tk
import video_library as lib
import font_manager as fonts

class CreateVideoList():
    def __init__(self, window):
        self.window = window
        self.window.geometry('860x650')
        self.window.title('Create Video List')

        self.video_list = []  # List to store video numbers

        # Upper - Video List
        self.lbl_list = tk.Label(self.window, text='Video List')
        self.lbl_list.grid(row=0, column=0, padx=10, pady=10, columnspan=3)

        self.video_listbox = tk.Listbox(self.window, width=55, height=10, selectmode=tk.SINGLE)
        self.video_listbox.grid(row=1, column=0, columnspan=3, rowspan=5, sticky="W", padx=10, pady=10)
        self.video_listbox.bind("<<ListboxSelect>>", self.video_item_selected)

        # Lower - Playlist
        self.lbl_playlist = tk.Label(self.window, text='Playlist')
        self.lbl_playlist.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

        self.playlist_listbox = tk.Listbox(self.window, width=55, height=10, selectmode=tk.SINGLE)
        self.playlist_listbox.grid(row=7, column=0, columnspan=2, rowspan=5, sticky="W", padx=10, pady=10)
        self.playlist_listbox.bind("<<ListboxSelect>>", self.playlist_item_selected)


        # Right side - Video Entry and Buttons
        self.lbl_vid_num = tk.Label(self.window, text='Video Number')
        self.lbl_vid_num.grid(row=1, column=3, padx=10, pady=10)

        self.txt_vid_num = tk.Entry(self.window, width=3)
        self.txt_vid_num.grid(row=2, column=3, padx=10, pady=10)

        self.add_to_playlist_btn = tk.Button(self.window, text="Add to Playlist",width=18, command=self.add_to_playlist)
        self.add_to_playlist_btn.grid(row=3, column=3, padx=10, pady=10)

        self.play_playlist_btn = tk.Button(self.window, text="Play Playlist", width=18, command=self.play_playlist)
        self.play_playlist_btn.grid(row=7, column=3, padx=10, pady=10)

        self.remove_from_playlist_btn = tk.Button(self.window, text="Remove from Playlist", width=18, command=self.remove_from_playlist)
        self.remove_from_playlist_btn.grid(row=8, column=3, padx=10, pady=10)

        self.clear_playlist_btn = tk.Button(self.window, text="Clear Playlist",width=18, command=self.clear_playlist)
        self.clear_playlist_btn.grid(row=9, column=3, padx=10, pady=10)

        self.list_videos_clicked()  # Automatically load the video list when the window is opened


    def remove_from_playlist(self):
        selected_index = self.playlist_listbox.curselection()
        if selected_index:
            removed_item = self.playlist_listbox.get(selected_index[0])
            self.playlist_listbox.delete(selected_index[0])
            print(f"Removed from Playlist: {removed_item}")


    def play_playlist(self):
        for video_number in self.video_list:
            increment_play_count(video_number)

    def increment_play_count(key):
        try:
            item = library[key]
            item.play_count += 1
        except KeyError:
            return

    def add_to_playlist(self):
        if self.video_listbox.curselection():  # Check if the video is selected from the listbox
            video_number = self.video_list[self.video_listbox.curselection()[0]]
        else:
            video_number = self.txt_vid_num.get()  # If no video is selected from the listbox, use the video number from the entry field

        video_name = lib.get_name(video_number)  # Convert video_number to a string

        if video_name:
            self.video_list.append(video_number)  # Add video number to the list
            self.update_playlist_text() 
        else:
            print("Video not found")


    def update_playlist_text(self):
        video_number = self.video_list[-1]
        video_name = lib.get_name(str(self.video_list[-1]))  # Convert video_number to a string
        video_director = lib.get_director(str(self.video_list[-1]))
        self.playlist_listbox.insert(tk.END, f'{video_number} - {video_name} - {video_director}')

        

    def clear_playlist(self):
        self.video_list = []  # Clear the list
        self.playlist_listbox.delete(0, tk.END)
        

    def list_videos_clicked(self):
        # Instead of calling lib.list_all(), we'll use the keys from the library dictionary
        video_list = lib.library.keys()
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
