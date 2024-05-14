import csv
import tkinter as tk
from tkinter import ttk,filedialog
from PIL import Image, ImageTk
import os
from AAAA import ReviewsTab
import library_item as lib
import video_library as lib
import font_manager as fonts
import tkinter.scrolledtext as tkst
from tkinter import messagebox as msb


class PlayList_UpdateVideos():
    def __init__(self, window):
        self.window = window
        self.window.geometry('1200x850')
        self.window.title('Create Video List')
        
        self.playlist = []

        ###MAIN BUTTONS 
        self.back_to_menu_btn = tk.Button(self.window, text="Back to Menu", width=11, command=self.back_to_menu)
        self.back_to_menu_btn.grid(row=0, column=0, padx=10, pady=10, sticky="W")

        ####VIDEO LIST AND INFORMATION FRAME

        self.video_list_info_frame = tk.Frame(self.window, borderwidth=5, relief="sunken")
        self.video_list_info_frame.grid(row=1, column=0, columnspan=5, rowspan=6, padx=10, pady=10, sticky="nsew")

        # Upper - Video List
        self.lbl_list = ttk.Label(self.video_list_info_frame, text='Video List')
        self.lbl_list.grid(row=0, column=0, padx=10, pady=10, columnspan=3)
        
        self.video_listbox = tk.Listbox(self.video_list_info_frame, width=55, height=10, selectmode=tk.SINGLE)
        self.video_listbox.grid(row=1, column=0, columnspan=3, rowspan=5, sticky="W", padx=10, pady=10)
        self.video_listbox.bind("<<ListboxSelect>>", self.video_item_selected)

        ### VIDEO INFORMATION FRAME
        self.cover_photo = tk.Label(self.video_list_info_frame, text='Video Information')
        self.cover_photo.grid(row=0, column=4, columnspan=3, padx=10, pady=10)

        self.video_info_frame = tk.Frame(self.video_list_info_frame, borderwidth=5, relief="groove")
        self.video_info_frame.grid(row=1, column=3,columnspan=5, rowspan=5, padx=10, pady=10, sticky="nsew")

        self.video_name_frame = ttk.Frame(self.video_info_frame)
        self.video_name_frame.grid(row=1, column=1, rowspan=3, padx=10, pady=10, sticky="W")

        self.cover_frame = ttk.Frame(self.video_info_frame,borderwidth=5, relief="raised")
        self.cover_frame.grid(row=1, column=3,columnspan=4, rowspan=3, padx=10, pady=10, sticky='e')

        self.cover_photo_label = tk.Label(self.cover_frame)
        self.cover_photo_label.grid(row=0, column=0)

        self.video_name_label = tkst.ScrolledText(self.video_name_frame, width=20, height=12, wrap="word")
        self.video_name_label.grid(row=1, column=5, padx=10, pady=10)

        self.video_name_label.config(width=27)

        self.error_label = tk.Label(self.window, text="", font=("Helvetica", 10), fg="red")
        self.error_label.grid(row=2, column=0, columnspan=3, padx=10, pady=10)
        
        # Create a notebook (tabbed interface)
        self.notebook = ttk.Notebook(self.window)
        self.notebook.grid(row=7, column=0, columnspan=3, padx=10, pady=10)

        self.create_playlist_tab()
        # self.create_review_tab()
        
        # Display video list
        self.list_videos_clicked()
        ReviewsTab(self.notebook)

    def create_playlist_tab(self):
        #PLAYLIST TAB
        playlist_frame = ttk.Frame(self.notebook)
        self.notebook.add(playlist_frame, text='Playlist', padding=5)

        #PLAYLIST WIDGET
        lbl_playlist = tk.Label(playlist_frame, text='Playlist')
        lbl_playlist.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.playlist_listbox = tk.Listbox(playlist_frame, width=55, height=10, selectmode=tk.SINGLE)
        self.playlist_listbox.grid(row=1, column=0, columnspan=2, rowspan=5, sticky="W", padx=10, pady=10)

        add_to_playlist_btn = tk.Button(playlist_frame, text="Add to Playlist", width=18, command=self.add_to_playlist)
        add_to_playlist_btn.grid(row=2, column=3, padx=10, pady=10)

        play_playlist_btn = tk.Button(playlist_frame, text="Play Playlist", width=18, command=self.play_playlist)
        play_playlist_btn.grid(row=3, column=3, padx=10, pady=10)

        remove_from_playlist_btn = tk.Button(playlist_frame, text="Remove from Playlist", width=18,command=self.remove_from_playlist)
        remove_from_playlist_btn.grid(row=4, column=3, padx=10, pady=10)

        clear_playlist_btn = tk.Button(playlist_frame, text="Clear Playlist", width=18, command=self.clear_playlist)
        clear_playlist_btn.grid(row=4, column=4, padx=10, pady=10)

        save_playlist_btn = tk.Button(playlist_frame, text="Save Playlist", width=18, command=self.save_playlist)
        save_playlist_btn.grid(row=2, column=4, padx=10, pady=10)

        load_playlist_btn = tk.Button(playlist_frame, text="Load Playlist", width=18, command=self.load_playlist)
        load_playlist_btn.grid(row=3, column=4, padx=10, pady=10)

        self.vid_num_frame = ttk.Frame(playlist_frame, borderwidth=5, relief='ridge')
        self.vid_num_frame.grid(row=1, column=3, columnspan=2, padx=10, pady=10)

        self.lbl_vid_num = tk.Label(self.vid_num_frame, text='Video Number')
        self.lbl_vid_num.grid(row=0, column=1, padx=10, pady=10)

        self.txt_vid_num = tk.Entry(self.vid_num_frame, width=10) #entry box to  enter video number to be added to playlist
        self.txt_vid_num.grid(row=0, column=2, padx=10, pady=10, sticky='w')

        self.total_duration = 0

        self.total_duration_var = tk.StringVar()
        self.total_duration_label = tk.Label(playlist_frame,textvariable=self.total_duration_var, font=("Helvetica", 15), fg="blue")
        self.total_duration_label.grid(row=0, column=3, columnspan=3, padx=10, pady=10)

        self.update_total_duration()

    def rate_video_clicked(self):
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
            msb.showinfo('Success', 'Playlist saved successfully')
            print(f"Playlist saved to {file_path}")

    def load_playlist(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])

        if file_path:
            
            self.clear_playlist() #Clear the current playlist

            #Open the file in read mode
            with open(file_path, 'r') as csvfile:
                
                csv_reader = csv.reader(csvfile) #Create a CSV reader object
                
                next(csv_reader, None) #Skip the header row

                #Read each row and add the video to the playlist
                for row in csv_reader:
                    video_number, video_name, video_director = row
                    playlist_item = f"{video_number} - {video_name} - {video_director}"
                    self.playlist_listbox.insert(tk.END, playlist_item)

            msb.showinfo('Success', 'Playlist loaded successfully')
            print(f"Playlist loaded from {file_path}")

        else:
            msb.showerror('Error', 'No file selected')


    def back_to_menu(self):
        from video_player import VideoPlayer
        VideoPlayer(tk.Toplevel(window))

    def remove_from_playlist(self):
        selected_index = self.playlist_listbox.curselection()
        if selected_index:
            removed_item = self.playlist_listbox.get(selected_index[0])
            video_number = removed_item.split(' ')[0]
            video_duration = lib.get_duration(video_number)

            self.total_duration -= video_duration #Subtract the duration of the removed video
            self.update_total_duration() #Update the total duration label

            self.playlist_listbox.delete(selected_index[0]) #Remove the item from the playlist
            print(f"Removed from Playlist: {removed_item}")
        else:
            msb.showerror('Error', 'No item selected')


    def play_playlist(self):
        for playlist_item in self.playlist_listbox.get(0, tk.END):
            video_number = playlist_item.split(' ')[0]
            if lib.get_name(video_number):  #Check if the video is in the library
                lib.increment_play_count(video_number)
                msb.showinfo("Success", f"Playing video {video_number} - Play count: {lib.get_play_count(video_number)}")

    def update_total_duration(self):
        hours, minutes = divmod(self.total_duration, 60)
        self.total_duration_var.set(f"Total Duration: {hours} hours {minutes} minutes")

    def add_to_playlist(self):
        if self.video_listbox.curselection():  #Check if the video is selected from the listbox
            video_number = self.video_list[self.video_listbox.curselection()[0]]
        else:
            video_number = self.txt_vid_num.get().strip()  #If no video is selected from the listbox, use the video number from the entry field
        

        video_name = lib.get_name(video_number)
        video_duration = lib.get_duration(video_number)

        if video_name:
            if video_number not in self.playlist:
                self.playlist.append(video_number)  #Add video number to the list
            else:
                msb.showerror("Error", "Video already in playlist")
                return

            #Update total duration
            self.total_duration += video_duration
            self.update_total_duration()

            self.update_playlist_text()

        else:
            msb.showerror("Error", "Video not found")

    def display_cover_photo(self, video_number):
        script_directory = os.path.dirname(os.path.abspath(__file__))
        cover_photo_path = script_directory + '/' + "covers" + '/' + str(video_number) + '.jpg'

        try:
            image = Image.open(cover_photo_path)
            image.thumbnail((150, 200))
        except FileNotFoundError as e:
            msb.showerror('Error', f"Cover photo not found for video number {video_number}")
            return

        photo = ImageTk.PhotoImage(image)# Convert the Image object to a PhotoImage object
        
        self.cover_photo_label.config(image=photo, width=150, height=200)# Update the PhotoImage of the cover photo label
        self.cover_photo_label.image = photo


    def update_playlist_text(self):
        if self.playlist:
            video_number = self.playlist[-1]
            video_name = lib.get_name(str(video_number))  # Convert video_number to a string
            video_director = lib.get_director(str(video_number))
            self.playlist_listbox.insert(tk.END, f'{video_number} - {video_name} - {video_director}')
            # Call the display_cover_photo method with the video number
            # Assuming you have a display_cover_photo method, modify the line as needed
            self.show_video_info(video_number)

    def clear_playlist(self):
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
            self.display_cover_photo(video_number)
        except KeyError:
            msb.showerror('Error', f"Video not found for number {video_number}")

    def list_videos_clicked(self):
        video_list = lib.library.keys()
        self.video_listbox.delete(0, tk.END)
        self.video_list = list(video_list)
        for video_number in video_list:
            video_name = lib.get_name(str(video_number))
            video_director = lib.get_director(str(video_number))
            star_rating = lib.library[video_number].stars()
            self.video_listbox.insert(tk.END, f'{video_number} - {video_name} - {video_director} - Rating: {star_rating}')


    def update_video_reviews(self, video_number):
        # Update the video_review_list widget with all reviews for the selected video
        reviews = lib.get_reviews(video_number)
        self.video_review_list.delete("1.0", tk.END)  # Clear existing text

        for i, review in enumerate(reviews, start=1):
            self.video_review_list.insert(tk.END, f"{i}. {review}\n\n")
            
    def video_item_selected(self, event):
        selected_index = self.video_listbox.curselection()
        selected_video_number = self.video_list[selected_index[0]]

        # Call the display_cover_photo method with the selected video number
        self.show_video_info(str(selected_video_number))

        # Update the video_review_list with reviews for the selected video
        self.update_video_reviews(selected_video_number)

if __name__ == "__main__":
    window = tk.Tk()
    fonts.configure()
    PlayList_UpdateVideos(window)
    window.mainloop()



