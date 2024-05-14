import tkinter as tk
from tkinter import messagebox
import tkinter.scrolledtext as tkst
import font_manager as fonts
import video_library as lib 
from tkinter import ttk,filedialog

def set_text(text_area, content): #set text in a given text area
    text_area.delete("1.0", tk.END) #delete everything in the text area
    text_area.insert(1.0, content)  #insert the content

class UpdateVideo():
    def __init__(self, window):
        self.window = window
        self.window.geometry("900x400")
        self.window.title("Update Videos")

        self.__create_widgets()
        

    def __create_widgets(self):
        
        # self.__lbl_vid_number = tk.Label(self.window, text="Enter Video Number")
        # self.__lbl_vid_number.grid(row=1, column=0, padx=10, pady=10, sticky="W")

        # self.__txt_vid_number = tk.Entry(self.window, width=3)
        # self.__txt_vid_number.grid(row=1, column=1, padx=10, pady=10)

        # self.__btn_check = tk.Button(self.window, text="Check", command=self.check_video_clicked)
        # self.__btn_check.grid(row=1, column=2, padx=10, pady=10)

        # self.__lbl_new_rating = tk.Label(self.window, text="Enter New Rating")
        # self.__lbl_new_rating.grid(row=2, column=0, padx=10, pady=10, sticky="W")

        # self.__txt_new_rating = tk.Entry(self.window, width=3)
        # self.__txt_new_rating.grid(row=2, column=1, padx=10, pady=10)

        # self.__btn_update = tk.Button(self.window, text="Update", command= self.update_video_clicked)
        # self.__btn_update.grid(row=2, column=2,padx=10, pady=10)

        # self.video_txt = tk.Text(self.window, width=24, height=4, wrap="none") 
        # self.video_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)

        # self.status_lbl = tk.Label(self.window, text="", font=("Helvetica", 10))
        # self.status_lbl.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

        # self.review_box = tkst.ScrolledText(self.window)
        # self.review_box.grid(row=3, column=0, columnspan=4, padx=10, pady=10)
        self.back_to_menu = tk.Button(self.window, text="Back to Menu", command=self.back_to_menu)
        self.back_to_menu.grid(row=0, column=0, padx=10, pady=10)

        self.top_left_label = tk.Label(self.window, text="Videos List")
        self.top_left_label.grid(row=0, column=1, padx=10, pady=10)

        self.video_list = tk.Listbox(self.window, width=45, height=10, selectmode=tk.SINGLE)
        self.video_list.grid(row=1, column=0,columnspan=3, padx=10, pady=10)
        self.video_list.bind("<<ListboxSelect>>", self.video_list_clicked)

        self.top_right_label = tk.Label(self.window, text="Video Details")
        self.top_right_label.grid(row=0, column=4, columnspan=3, padx=10, pady=10)


        #top right frame

        self.video_info_frame = tk.Frame(self.window, borderwidth=5, relief="sunken")
        self.video_info_frame.grid(row=1, column=4,columnspan=3, rowspan=2, padx=10, pady=10, sticky="nsew")

        self.cover_frame = ttk.Frame(self.video_info_frame, style='TFrame',borderwidth=5, relief="raised")
        self.cover_frame.grid(row=0, column=1, rowspan=3, padx=10, pady=10)

        self.cover_photo_label = tk.Label(self.cover_frame)
        self.cover_photo_label.grid(row=1, column=2, sticky="nsew")
    
        self.video_name_frame = ttk.Frame(self.video_info_frame, style='TFrame')
        self.video_name_frame.grid(row=0, column=3, rowspan=3, padx=10, pady=10, sticky="W")

        self.video_name_label = tkst.ScrolledText(self.video_name_frame, width=18, height=12, wrap="word")
        self.video_name_label.grid(row=1, column=4, padx=10, pady=10)

        self.window.columnconfigure(3, weight=0)

        # Set the row weight for both the listbox and the cover photo frame to be the same
        self.window.rowconfigure(1, weight=1)

    def video_list_clicked(self, event):
        pass


    def back_to_menu(self):
        pass

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
            set_text(self.video_txt, f"Video {key} not found")
    def update_video_clicked(self):
        video_number = self.__txt_vid_number.get()
        new_rating = self.__txt_new_rating.get()

        if video_number and new_rating:
            if lib.get_rating(video_number):
                lib.set_rating(video_number, new_rating)
                messagebox.showinfo("Success", "Video updated successfully!")
                self.__txt_vid_number.delete(0, tk.END)
                self.__txt_new_rating.delete(0, tk.END)
                set_text(self.video_txt, "")
            else:
                set_text(self.video_txt, f"Video {video_number} not found")
        else:
            set_text(self.video_txt, "Please enter video number and new rating!")




if __name__ == "__main__":  # only runs when this file is run as a standalone
    window = tk.Tk()        # create a TK object
    fonts.configure()       # configure the fonts
    UpdateVideo(window)     
    window.mainloop()     