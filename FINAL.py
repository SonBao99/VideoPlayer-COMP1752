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
        self.create_review_tab()
        self.update_info()

        # Display video list
        self.list_videos_clicked()

    def update_info(self):
        self.update_info_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.update_info_frame, text ='Update Info')
        
        self.sample_label = tk.Label(self.update_info_frame, text = 'Video info')
        self.sample_label.grid(row = 0, column=0)

        self.sample_entry_box = tk.Entry(self.update_info_frame, width= 20)
        self.sample_entry_box.grid(row=0, column=1, columnspan= 3)

    def create_review_tab(self):
        #REVIEW TAB
        reviews_frame = ttk.Frame(self.notebook)
        self.notebook.add(reviews_frame, text='Reviews', padding=5)

        #REVIEW WIDGETS
        self.lbl_review = tk.Label(reviews_frame, text='Reviews')
        self.lbl_review.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        self.video_review_list = tkst.ScrolledText(reviews_frame, width=67, height=12)
        self.video_review_list.grid(row=1, column=0, columnspan=3, rowspan=4, padx=10, pady=10, sticky='nsew')

        self.lbl_new_review = tk.Label(reviews_frame, text="Enter Review")
        self.lbl_new_review.grid(row=2, column=4, padx=10, pady=10, sticky="W")

        self.txt_new_review = tkst.ScrolledText(reviews_frame, width=30, height=10)
        self.txt_new_review.grid(row=2, column=5, padx=10, pady=10, sticky="W")

        self.lbl_new_rating = tk.Label(reviews_frame, text="Select New Rating")
        self.lbl_new_rating.grid(row=1, column=4, padx=10, pady=10, sticky="W")

        ratings = [1, 2, 3, 4, 5]
        self.selected_rating = tk.StringVar(value=ratings[0])
        self.rating_dropdown = ttk.Combobox(reviews_frame, textvariable=self.selected_rating, values=ratings,state="readonly", width=6)
        self.rating_dropdown.grid(row=1, column=5, padx=10, pady=10, sticky="W")

        self.btn_update = tk.Button(reviews_frame, text="Rate", command=self.rate_video_clicked)
        self.btn_update.grid(row=1, column=5, padx=10, pady=10)

    def create_playlist_tab(self):
        #PLAYLIST TAB
        playlist_frame = ttk.Frame(self.notebook)
        self.notebook.add(playlist_frame, text='Playlist', padding=5)

        #PLAYLIST WIDGET
        self.lbl_playlist = tk.Label(playlist_frame, text='Playlist')
        self.lbl_playlist.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.playlist_listbox = tk.Listbox(playlist_frame, width=55, height=10, selectmode=tk.SINGLE)
        self.playlist_listbox.grid(row=1, column=0, columnspan=2, rowspan=5, sticky="W", padx=10, pady=10)
        self.playlist_listbox.bind("<<ListboxSelect>>", self.video_item_selected)

        self.add_to_playlist_btn = tk.Button(playlist_frame, text="Add to Playlist", width=18, command=self.add_to_playlist)
        self.add_to_playlist_btn.grid(row=2, column=3, padx=10, pady=10)

        self.play_playlist_btn = tk.Button(playlist_frame, text="Play Playlist", width=18, command=self.play_playlist)
        self.play_playlist_btn.grid(row=3, column=3, padx=10, pady=10)

        self.remove_from_playlist_btn = tk.Button(playlist_frame, text="Remove from Playlist", width=18,command=self.remove_from_playlist)
        self.remove_from_playlist_btn.grid(row=4, column=3, padx=10, pady=10)

        self.clear_playlist_btn = tk.Button(playlist_frame, text="Clear Playlist", width=18, command=self.clear_playlist)
        self.clear_playlist_btn.grid(row=4, column=4, padx=10, pady=10)

        self.save_playlist_btn = tk.Button(playlist_frame, text="Save Playlist", width=18, command=self.save_playlist)
        self.save_playlist_btn.grid(row=2, column=4, padx=10, pady=10)

        self.load_playlist_btn = tk.Button(playlist_frame, text="Load Playlist", width=18, command=self.load_playlist)
        self.load_playlist_btn.grid(row=3, column=4, padx=10, pady=10)

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
        selected_index = self.video_listbox.curselection() # Get the index of the selected video
        try:  
            video_number = self.video_list[selected_index[0]] #Get the video number
            new_rating = int(self.rating_dropdown.get())  # Get the new rating from the dropdown menu 
            new_rating_stars = "★" * new_rating  
            lib.set_rating(video_number, new_rating) # Update the rating
            new_review = self.txt_new_review.get("1.0", tk.END) # Get the new review from the text widget
            if new_review.strip():  # Check if the review is not empty or contains only whitespace
                lib.add_review(video_number, new_review)  # Add the new review
                msb.showinfo("Success", "Review and rating added successfully!")
            else:
                msb.showinfo("Success", "Rating updated successfully!")
            self.update_video_reviews(video_number)# Update the video_review_list widget with all reviews for the selected video
            # Update video list when press the rate button
            updated_item = self.video_listbox.get(selected_index[0]) # Get the updated item from the listbox
            video_name = lib.get_name(str(video_number)) # Get the video name
            video_director = lib.get_director(str(video_number)) # Get the video director
            updated_item = f'{video_number} - {video_name} - {video_director} - Rating: {new_rating_stars}' #Assign the video's info to 'updated item'
            self.video_listbox.delete(selected_index[0]) # Delete the old item selected video information from the listbox
            self.video_listbox.insert(selected_index[0], updated_item) # Insert the updated video info's rate at the same index

            self.txt_new_review.delete("1.0", tk.END) # Clear the text widget, 1.0 means start of the text, in this case, 1 is the line 
            #while 0 is the column, tk.END means end of the text 
        except IndexError:
            msb.showerror("Error", "Please select a video to rate")


    def save_playlist(self):
        if self.playlist == []: #If the playlist is empty
            msb.showerror('Error', 'Playlist is empty')
            return
        else:
            file_path = tk.filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")]) 
            with open(file_path, 'w', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                # Write the header row
                csv_writer.writerow(['Video Number', 'Video Name', 'Video Director'])
                # Write each playlist item to the CSV file
                for playlist_item in self.playlist_listbox.get(0, tk.END):
                    video_number = playlist_item.split(' ')[0]
                    video_name = lib.get_name(video_number)
                    video_director = lib.get_director(video_number)
                    csv_writer.writerow([video_number, video_name, video_director])# Write the video information to the CSV file
            msb.showinfo('Success', 'Playlist saved successfully')
            print(f"Playlist saved to {file_path}")


    def load_playlist(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if self.playlist != []: #If the playlist is not empty
            self.clear_playlist()# Clear the current playlist
        else:
        #Open the file in read mode
            with open(file_path, 'r') as csvfile:
                csv_reader = csv.reader(csvfile)# Create a CSV reader object
                next(csv_reader, None)# Skip the header row
                # Read each row and add the video to the playlist
                for row in csv_reader: # Read each row
                    video_number, video_name, video_director = row
                    playlist_item = f"{video_number} - {video_name} - {video_director}" 
                    self.playlist_listbox.insert(tk.END, playlist_item) #add the video to the playlist
            msb.showinfo('Success', 'Playlist loaded successfully') 
            print(f"Playlist loaded from {file_path}")


    def back_to_menu(self):
        from video_player import VideoPlayer
        VideoPlayer(tk.Toplevel(window))


    def remove_from_playlist(self):
        selected_index = self.playlist_listbox.curselection()
        if selected_index:  #If an item is selected in the playlist_listbox
            removed_item = self.playlist_listbox.get(selected_index)
            video_number = removed_item.split(' ')[0]
            video_duration = lib.get_duration(video_number)
            # Subtract the duration of the removed video
            self.total_duration -= video_duration
            # Update the total duration label
            self.update_total_duration()
            # Remove the video_number from the playlist
            self.playlist.remove(video_number)
            # Remove the item from the playlist_listbox
            self.playlist_listbox.delete(selected_index)
            msb.showinfo('Success', f'Removed video {video_number} - {lib.get_name(video_number)} - {lib.get_director(video_number)} from Playlist')
        else:  # If no item is selected in the playlist_listbox
            msb.showerror('Error', 'Please select a video from the playlist')


    def play_playlist(self):
        if self.playlist == []:
            msb.showerror('Error', 'Playlist is empty')
        else:
            for playlist_item in self.playlist_listbox.get(0, tk.END): 
                video_number = playlist_item.split()[0] # Extract the video number from the playlist item by splitting the string into substring such as [video_number, - , video_name, - , video_director] and taking the first part of the resulting list.
                lib.increment_play_count(video_number)
                msb.showinfo("Success", f"Playing video {video_number} - Play count: {lib.get_play_count(video_number)}")


    def update_total_duration(self):
        result = divmod(self.total_duration, 60) # Calculate the total duration in hours and minutes
        hours = result[0] #get the first index of the result
        minutes = result[1] # get the second index of the result
        self.total_duration_var.set(f"Total Duration: {hours} hours {minutes} minutes") # Update the total duration label


    def add_to_playlist(self):
        try:
            if self.video_listbox.curselection():
                video_number = self.video_list[self.video_listbox.curselection()[0]]
            else:
                # If no video is selected from the listbox, use the video number from the entry field instead.
                video_number = self.txt_vid_num.get().strip()
            # Check if the video number is already in the playlist
            if video_number not in self.playlist:
                self.playlist.append(video_number)  
            else:
                msb.showerror("Error", "Video already in playlist")
                return
            video_duration = lib.get_duration(video_number) # Get the duration of the video from the library
            self.total_duration += video_duration # Update total duration
            self.update_total_duration()  # Update the total duration label
            self.update_playlist_text()# Update the playlist listbox infomation
        except ValueError:
            msb.showerror("Error", "Invalid video number. Please enter a valid integer.")
        except IndexError:
            msb.showerror("Error", "No video selected from the listbox.")


    def display_cover_photo(self, video_number):
        script_directory = "c:\\Users\\baoso\\OneDrive - Thang Long University\\Máy tính\\Coursework\\OOP\\VideoPlayer COMP1752" 
        cover_photo_path = script_directory + '\\' + "covers" + '\\' + str(video_number) + '.jpg' # Construct the path to the cover photo
        try:
            image = Image.open(cover_photo_path) # Open the cover photo
            image.thumbnail((150, 200))  # Resize the cover photo
        except FileNotFoundError as e: # If the cover photo is not found
            msb.showerror('Error', f"Cover photo not found for video number {video_number}")
            return
        photo = ImageTk.PhotoImage(image)# Convert the Image object to a PhotoImage object
        self.cover_photo_label.config(image=photo, width=150, height=200)# Update the PhotoImage of the cover photo label
        self.cover_photo_label.image = photo # Update the PhotoImage each time the cover photo label is updated


    def update_playlist_text(self):
        video_number = self.playlist[-1]  # Get the last video number in the playlist
        video_name = lib.get_name(str(video_number))  # Convert video_number to a string
        video_director = lib.get_director(str(video_number))  # Convert video_number to a string
        self.playlist_listbox.insert(tk.END, f'{video_number} - {video_name} - {video_director}')  # Add the video to the playlist


    def clear_playlist(self):
        if self.playlist == []: # Check if the playlist is empty
            msb.showerror('Error', 'Playlist is already empty')# If the playlist is empty, show an error message
        else:
            self.playlist = [] #Reset the self.playlist list to an empty list
            self.playlist_listbox.delete(0, tk.END) # to delete all items in the Listbox. The first parameter is '0' which mean to start from the beginning of the list, 
            #and the second parameter is 'tk.END' which means to delete all items from the listbox.
            self.total_duration = 0 #Set the total duration back to zero and update the total duration label in the UI.
            self.update_total_duration() 
            msb.showinfo('Success', 'Playlist cleared')


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
        video_list = lib.library.keys()  # Get a list of all video numbers
        self.video_listbox.delete(0, tk.END)  # Clear the video_listbox
        self.video_list = list(video_list)  # Convert video_list to a list
        for video_number in video_list:  
            video_name = lib.get_name(str(video_number)) 
            video_director = lib.get_director(str(video_number))
            star_rating = lib.library[video_number].stars()
            self.video_listbox.insert(tk.END, f'{video_number} - {video_name} - {video_director} - Rating: {star_rating}')


    def update_video_reviews(self, video_number):
        # Update the video_review_list widget with all reviews for the selected video
        reviews = lib.get_reviews(video_number)
        self.video_review_list.delete("1.0", tk.END)  # Clear existing text

        for i, review in enumerate(reviews, start=1):   #for each review in "reviews", iterate through the list starting from 1
            self.video_review_list.insert(tk.END, f"{i}. {review}\n\n") # insert the review into the video_review_list widget followed by a blank line, /
            #each reveiw start with an index 


    def video_item_selected(self, event):
        selected_index_video_list = self.video_listbox.curselection()
        selected_index_playlist = self.playlist_listbox.curselection()
        if selected_index_video_list:  # Check if selected_index is not empty
            selected_video_number = self.video_list[selected_index_video_list[0]]
            # Call the display_cover_photo method with the selected video number
            self.show_video_info(selected_video_number)
            # Update the video_review_list with reviews for the selected video
            self.update_video_reviews(selected_video_number)
        else:
            selected_video_number = self.playlist[selected_index_playlist[0]]
            self.show_video_info(selected_video_number)
            self.update_video_reviews(selected_video_number)


if __name__ == "__main__":
    window = tk.Tk()
    fonts.configure()
    PlayList_UpdateVideos(window)
    window.mainloop()