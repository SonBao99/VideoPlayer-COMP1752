import csv
import tkinter as tk
from tkinter import ttk,filedialog
from PIL import Image, ImageTk

import os

import library_item as lib
import video_library as lib
import font_manager as fonts
import tkinter.scrolledtext as tkst
from tkinter import messagebox as msb

class CreateVideoList():
    def __init__(self, window):
        self.window = window
        self.window.geometry('1100x650')
        self.window.title('Create Video List')

        self.video_list = []  # List to store video numbers

        # Upper - Video List
        self.lbl_list = ttk.Label(self.window, text='Video List')
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

        self.cover_photo = tk.Label(self.window, text='Video Information')
        self.cover_photo.grid(row=0, column=3, columnspan=2, padx=10, pady=10)

        #styles
        style = ttk.Style()
        style.configure("TFrame", background="#EAEAEA", padding=(5, 5))

        # Right side - Video Entry and Buttons

        self.vid_num_frame = ttk.Frame(self.window, borderwidth=5, relief='ridge')
        self.vid_num_frame.grid(row=7, column=3, columnspan=2, padx=10, pady=10)

        self.lbl_vid_num = tk.Label(self.vid_num_frame, text='Video Number')
        self.lbl_vid_num.grid(row=7, column=3, padx=10, pady=10)

        self.txt_vid_num = tk.Entry(self.vid_num_frame, width=10)
        self.txt_vid_num.grid(row=7, column=4, padx=10, pady=10, sticky='w')

        self.add_to_playlist_btn = tk.Button(self.window, text="Add to Playlist", width=18, command=self.add_to_playlist)
        self.add_to_playlist_btn.grid(row=8, column=3, padx=10, pady=10)

        self.play_playlist_btn = tk.Button(self.window, text="Play Playlist", width=18, command=self.play_playlist)
        self.play_playlist_btn.grid(row=9, column=3, padx=10, pady=10)

        self.remove_from_playlist_btn = tk.Button(self.window, text="Remove from Playlist", width=18, command=self.remove_from_playlist)
        self.remove_from_playlist_btn.grid(row=10, column=3, padx=10, pady=10)

        self.clear_playlist_btn = tk.Button(self.window, text="Clear Playlist", width=18, command=self.clear_playlist)
        self.clear_playlist_btn.grid(row=10, column=4, padx=10, pady=10)

        self.save_playlist_btn = tk.Button(self.window, text="Save Playlist", width=18, command=self.save_playlist)
        self.save_playlist_btn.grid(row=8, column=4, padx=10, pady=10)

        self.load_playlist_btn = tk.Button(self.window, text="Load Playlist", width=18, command=self.load_playlist)
        self.load_playlist_btn.grid(row=9, column=4, padx=10, pady=10)


        #Top right

        
        self.video_info_frame = tk.Frame(self.window, borderwidth=5, relief="sunken")
        self.video_info_frame.grid(row=1, column=3,columnspan=2, rowspan=5, padx=10, pady=10, sticky="nsew")

        self.cover_frame = ttk.Frame(self.window, style='TFrame',borderwidth=5, relief="raised")
        self.cover_frame.grid(row=1, column=3, rowspan=3, padx=10, pady=10)

        self.cover_photo_label = tk.Label(self.cover_frame)
        self.cover_photo_label.grid(row=0, column=0, sticky="nsew")
    
        self.video_name_frame = ttk.Frame(self.window, style='TFrame')
        self.video_name_frame.grid(row=1, column=4, rowspan=3, padx=10, pady=10, sticky="W")

        self.video_name_label = tkst.ScrolledText(self.video_name_frame, width=18, height=12, wrap="word")
        self.video_name_label.grid(row=1, column=5, padx=10, pady=10)

        self.window.columnconfigure(3, weight=0)

        # Set the row weight for both the listbox and the cover photo frame to be the same
        self.window.rowconfigure(1, weight=1)


        # Back to menu
        self.back_to_menu_btn = tk.Button(self.window, text="Back to Menu", width=11, command=self.back_to_menu)
        self.back_to_menu_btn.grid(row=0, column=0, padx=10, pady=10, sticky="W")

        self.list_videos_clicked()  # Automatically load the video list when the window is opened
        




    def save_playlist(self):
        file_path = tk.filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])

        if file_path:
            # Open the file in write mode
            with open(file_path, 'w', newline='') as csvfile:
                # Create a CSV writer object
                csv_writer = csv.writer(csvfile)

                # Write the header row
                csv_writer.writerow(['Video Number', 'Video Name', 'Video Director'])

                # Write each playlist item to the CSV file
                for playlist_item in self.playlist_listbox.get(0, tk.END):
                    video_number = playlist_item.split(' ')[0]
                    video_name = lib.get_name(video_number)
                    video_director = lib.get_director(video_number)

                    # Write the video information to the CSV file
                    csv_writer.writerow([video_number, video_name, video_director])
            msb.INFO('Success', 'Playlist saved successfully')
            print(f"Playlist saved to {file_path}")

    def load_playlist(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])

        if file_path:
            # Clear the current playlist
            self.clear_playlist()

            # Open the file in read mode
            with open(file_path, 'r') as csvfile:
                # Create a CSV reader object
                csv_reader = csv.reader(csvfile)

                # Skip the header row
                next(csv_reader, None)

                # Read each row and add the video to the playlist
                for row in csv_reader:
                    video_number, video_name, video_director = row
                    playlist_item = f"{video_number} - {video_name} - {video_director}"
                    self.playlist_listbox.insert(tk.END, playlist_item)

            msb.showinfo('Success', 'Playlist loaded successfully')
            print(f"Playlist loaded from {file_path}")

        else:
            print("No file selected.")


    def back_to_menu(self):
        from video_player import VideoPlayer
        VideoPlayer(tk.Toplevel(self.window))

    def remove_from_playlist(self):
        selected_index = self.playlist_listbox.curselection()
        if selected_index:
            removed_item = self.playlist_listbox.get(selected_index[0])
            self.playlist_listbox.delete(selected_index[0])
            print(f"Removed from Playlist: {removed_item}")

    def play_playlist(self):
        for playlist_item in self.playlist_listbox.get(0, tk.END):
            video_number = playlist_item.split(' ')[0]
            if lib.get_name(video_number):  # Check if the video is in the library
                lib.increment_play_count(video_number)
                print(f"Playing video {video_number} - Play count: {lib.get_play_count(video_number)}")
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


    def display_cover_photo(self, video_number):
        base_path = r"C:\Users\baoso\OneDrive - Thang Long University\Máy tính\Coursework\OOP\VideoPlayer COMP1752\covers"
        cover_photo_path = os.path.join(base_path, f"{video_number}.jpg")

        try:
            image = Image.open(cover_photo_path)
            # Maintain the aspect ratio while resizing
            image.thumbnail((150, 200))
        except FileNotFoundError as e:
            print(f"Cover photo not found for video number {video_number}")
            print(f"Error: {e}")
            # Display a placeholder image
            image = Image.new('RGB', (150, 200), color='gray')

        # Convert the Image object to a PhotoImage object
        photo = ImageTk.PhotoImage(image)

        # Update the PhotoImage of the cover photo label
        self.cover_photo_label.config(image=photo)
        self.cover_photo_label.image = photo


    def update_playlist_text(self):
        video_number = self.video_list[-1]
        video_name = lib.get_name(str(self.video_list[-1]))  # Convert video_number to a string
        video_director = lib.get_director(str(self.video_list[-1]))
        self.playlist_listbox.insert(tk.END, f'{video_number} - {video_name} - {video_director}')
        # Call the display_cover_photo method with the video number
        self.display_cover_photo(str(video_number))

    def clear_playlist(self):
        self.video_list = []  # Clear the list
        self.playlist_listbox.delete(0, tk.END)

    def show_video_info(self, video_number):
        try:
            # Retrieve LibraryItem based on the video number
            video_item = lib.library[video_number]

            # Create a string with video information
            info_text = f"Name: {video_item.name}\n\n"
            info_text += f"Director: {video_item.director}\n\n"
            info_text += f"Rating: {video_item.stars()} ({video_item.rating})\n\n"
            info_text += f"Play Count: {video_item.play_count}\n\n"
            # # Assuming duration is available in LibraryItem, adjust as needed
            info_text += f"Duration: {video_item.duration} minutes\n\n"
            info_text += f"Short Description: {video_item.short_description}"

            # Set the text in the video_name_label (ScrolledText)
            self.video_name_label.delete(1.0, tk.END)  # Clear existing text
            self.video_name_label.insert(tk.END, info_text)
        except KeyError:
            print(f"Video not found for number {video_number}")

    def list_videos_clicked(self):
        video_list = lib.library.keys()
        self.video_listbox.delete(0, tk.END)
        self.video_list = list(video_list)
        for video_number in video_list:
            video_name = lib.get_name(str(video_number))
            video_director = lib.get_director(str(video_number))
            star_rating = lib.library[video_number].stars()
            self.video_listbox.insert(tk.END, f'{video_number} - {video_name} - {video_director} - Rating: {star_rating}')

    def video_item_selected(self, event):
        
        selected_index = self.video_listbox.curselection()
        if selected_index:
            selected_video_number = self.video_list[selected_index[0]]
            selected_item = self.video_listbox.get(selected_index[0])
            print(f"Selected Video: {selected_item}")
            
            # Call the display_cover_photo method with the selected video number
            self.show_video_info(str(selected_video_number))
            self.display_cover_photo(str(selected_video_number))
        else:
            print("No video selected")

    def playlist_item_selected(self, event):
        selected_index = self.playlist_listbox.curselection()
        if selected_index:
            selected_item = self.playlist_listbox.get(selected_index[0])
            print(f"Selected Item: {selected_item}")
        else:
            print("No item selected")

if __name__ == "__main__":
    window = tk.Tk()
    fonts.configure()
    CreateVideoList(window)
    window.mainloop()



