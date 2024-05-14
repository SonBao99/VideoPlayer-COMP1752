import tkinter as tk
import font_manager as fonts
from check_videos import CheckVideos
from update_videos import UpdateVideo
from create_video_list import CreateVideoList

class VideoPlayer:
    def __init__(self,window):
        self.window = window
        self.window.geometry("520x150")
        self.window.title("Video Player")

        fonts.configure()

        self.header_lbl = tk.Label(self.window, text="Select an option by clicking one of the buttons below")
        self.header_lbl.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        self.check_videos_btn = tk.Button(self.window, text="Check Videos", command=self.check_videos_clicked)
        self.check_videos_btn.grid(row=1, column=0, padx=10, pady=10)

        self.create_video_list_btn = tk.Button(self.window, text="Create Video List", command=self.create_video_list_clicked)
        self.create_video_list_btn.grid(row=1, column=1, padx=10, pady=10)

        self.update_videos_btn = tk.Button(self.window, text="Update Videos", command=self.update_video_clicked)
        self.update_videos_btn.grid(row=1, column=2, padx=10, pady=10)

        self.status_lbl = tk.Label(self.window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

        self.window.mainloop()

    def check_videos_clicked(self):
        self.status_lbl.configure(text="Check Videos button was clicked!")
        CheckVideos(tk.Toplevel(self.window))

    def update_video_clicked(self):
        self.status_lbl.configure(text="Update Videos button was clicked!")
        UpdateVideo(tk.Toplevel(self.window))

    def create_video_list_clicked(self):
        self.status_lbl.configure(text="Create Video List button was clicked!")
        CreateVideoList(tk.Toplevel(self.window))

if __name__ == "__main__":
    window = tk.Tk()
    fonts.configure()
    VideoPlayer(window)
    window.mainloop()
