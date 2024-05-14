import tkinter as tk
import video_library as lib
import font_manager as fonts
from tkinter import messagebox as msb


class CreateVideoList():
    def __init__(self, window):
        self.window = window
        self.window.geometry('860x650')
        self.window.title('Create Video List')

        self.playlist_list = []  #List to store video numbers

        #Upper - Video List
        self.lbl_list = tk.Label(self.window, text='Video List')
        self.lbl_list.grid(row=0, column=0, padx=10, pady=10, columnspan=3)

        self.video_listbox = tk.Listbox(self.window, width=55, height=10, selectmode=tk.SINGLE)
        self.video_listbox.grid(row=1, column=0, columnspan=3, rowspan=5, sticky="W", padx=10, pady=10)
        self.video_listbox.bind("<<ListboxSelect>>", self.video_item_selected)

        #Lower - Playlist
        self.lbl_playlist = tk.Label(self.window, text='Playlist')
        self.lbl_playlist.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

        self.playlist_listbox = tk.Listbox(self.window, width=55, height=10, selectmode=tk.SINGLE)
        self.playlist_listbox.grid(row=7, column=0, columnspan=2, rowspan=5, sticky="W", padx=10, pady=10)
        self.playlist_listbox.bind("<<ListboxSelect>>", self.playlist_item_selected)

        #Right side - Video Entry and Buttons
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

        # Back to menu
        self.back_to_menu_btn = tk.Button(self.window, text="Back to Menu", width=11, command=self.back_to_menu)
        self.back_to_menu_btn.grid(row=0, column=0, padx=10, pady=10, sticky="W")

        self.list_videos_clicked()  # Automatically load the video list when the window is opened

    def back_to_menu(self):
        from video_player import VideoPlayer
        VideoPlayer(tk.Toplevel(self.window))
        

    def remove_from_playlist(self):
        # selected_index = self.playlist_listbox.curselection()
        # if selected_index:
        #     removed_item = self.playlist_listbox.get(selected_index[0])
        #     self.playlist_listbox.delete(selected_index[0])
        #     print(f"Removed from Playlist: {removed_item}")

        # video_number = self.txt_vid_num.get()
        # self.playlist_list.remove(video_number)
        # self.playlist_listbox.delete(0, tk.END)
        # print(f' remain: {self.playlist_list}')
        # msb.showinfo('Success', 'Removed from Playlist')
        
        video_number = self.txt_vid_num.get()

        # Check if video_number is in the playlist_list
        if video_number in self.playlist_list:
            # Remove the video_number from the playlist_list
            self.playlist_list.remove(video_number)

            # Update the Listbox with the updated playlist
            self.playlist_listbox.delete(0, tk.END)
            for item in self.playlist_list:
                self.playlist_listbox.insert(tk.END, item)

            print(f'Remaining in Playlist: {self.playlist_list}')
            msb.showinfo('Success', 'Removed from Playlist')
        else:
            msb.showerror('Error', 'Video not found in Playlist')

            
    def play_playlist(self):
        print(self.playlist_list)
        for video_number in self.playlist_list:
            if lib.get_name(video_number):  # Check if the video is in the library
                lib.increment_play_count(video_number)
                msb.showinfo("Success", f"Playing video {video_number} - Play count: {lib.get_play_count(video_number)}")

    def add_to_playlist(self):
        video_number = self.txt_vid_num.get()
        video_name = lib.get_name(video_number)  # Convert video_number to a string
        video_director = lib.get_director(video_number)

        try:
            video_number = int(video_number)
        except ValueError:
            msb.showerror("Error", "Please enter a valid integer for the video number")
            return
        
        if video_name:
            if video_number not in self.playlist_list:
                self.playlist_list.append(video_number)  # Add video number to the list
            else:
                msb.showerror("Error", "Video already in playlist")
                return
            self.playlist_listbox.insert(tk.END, f'{video_number} - {video_name} - {video_director}') 
            print(self.playlist_list)  # Print the updated playlist
        else:
            msb.showerror("Error", "Video not found in library")


    def clear_playlist(self):
        self.playlist_list = []  # Clear the list
        self.playlist_listbox.delete(0, tk.END)
        msb.showinfo('Success', 'Playlist cleared successfully')


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
            return "★" * int(rating)


if __name__ == "__main__":
    window = tk.Tk()
    fonts.configure()
    CreateVideoList(window)
    window.mainloop()


    def main():
        pass
