import tkinter as tk   #import tkinter library and all its classes, assign it as 'tk'
import tkinter.scrolledtext as tkst #import scrolled text from tkinter library and assign it as 'tkst'


import video_library as lib 
import font_manager as fonts 


def set_text(text_area, content): #set text in a given text area
    text_area.delete("1.0", tk.END) #delete everything in the text area
    text_area.insert(1.0, content)  #insert the content


class CheckVideos():            #Create class CheckVideos
    def __init__(self, window): #Constructor
        window.geometry("750x350") #set window size
        window.title("Check Videos") #set window title

        list_videos_btn = tk.Button(window, text="List All Videos", command=self.list_videos_clicked)   #create a button that will call the list_videos_clicked function
        list_videos_btn.grid(row=0, column=0, padx=10, pady=10) #set the button on the window using grid

        enter_lbl = tk.Label(window, text="Enter Video Number") #create a label that will display "Enter Video Number"
        enter_lbl.grid(row=0, column=1, padx=10, pady=10) #set the label on the window using grid

        self.input_txt = tk.Entry(window, width=3) #create an entry box to input video number
        self.input_txt.grid(row=0, column=2, padx=10, pady=10) #set the entry box on the window using grid

        check_video_btn = tk.Button(window, text="Check Video", command=self.check_video_clicked)  #Create a button that will call the check_video_clicked function
        check_video_btn.grid(row=0, column=3, padx=10, pady=10)     #set the button on the window using grid

        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none")     
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        self.video_txt = tk.Text(window, width=24, height=4, wrap="none") 
        self.video_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)

        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10)) #create a label that will display font type
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10) #set the label on the window using grid

        self.list_videos_clicked()  #call the list_videos_clicked function

    def check_video_clicked(self): #
        key = self.input_txt.get() #get the video number and assign it as 'key'
        name = lib.get_name(key) 
        if name is not None:
            director = lib.get_director(key)
            rating = lib.get_rating(key)
            play_count = lib.get_play_count(key)
            video_details = f"{name}\n{director}\nrating: {rating}\nplays: {play_count}"
            set_text(self.video_txt, video_details)
        else:
            set_text(self.video_txt, f"Video {key} not found")
        self.status_lbl.configure(text="Check Video button was clicked!")

    def list_videos_clicked(self):
        video_list = lib.list_all()
        set_text(self.list_txt, video_list)
        self.status_lbl.configure(text="List Videos button was clicked!")

if __name__ == "__main__":  # only runs when this file is run as a standalone
    window = tk.Tk()        # create a TK object
    fonts.configure()       # configure the fonts
    CheckVideos(window)     # open the CheckVideo GUI
    window.mainloop()       # run the window main loop, reacting to button presses, etc
