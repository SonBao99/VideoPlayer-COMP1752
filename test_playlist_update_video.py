import unittest
import tkinter as tk
from tkinter import ttk, scrolledtext
from unittest.mock import patch
from playlist_update_video import PlayList_UpdateVideos  
import video_library as lib


class TestPlayListUpdateVideos(unittest.TestCase):
    def setUp(self):
        self.window = tk.Tk()
        self.playlist_updater = PlayList_UpdateVideos(self.window)

    def tearDown(self):
        self.window.destroy()

    def test_initialization(self):
        try:
            # Ensure the window is created
            assert self.playlist_updater.window is not None

            # Ensure the notebook is created
            assert self.playlist_updater.notebook is not None

            # Ensure the video list is empty initially
            assert self.playlist_updater.video_list == []

            # Ensure total duration is 0 initially
            assert self.playlist_updater.total_duration == 0
        except AssertionError as e:
            self.fail(str(e))

    def test_add_to_playlist_valid_video(self):
        try:
            # Mocking the user input
            self.playlist_updater.txt_vid_num.insert(tk.END, "01")
            self.playlist_updater.add_to_playlist()

            # Assert that the video is added to the playlist
            assert len(self.playlist_updater.video_list) == 1
        except AssertionError as e:
            self.fail(str(e))

    def test_add_to_playlist_invalid_video(self):
        try:
            # Mocking the user input
            self.playlist_updater.txt_vid_num.insert(tk.END, "invalid_video_number")
            self.playlist_updater.add_to_playlist()

            # Assert that the video is not added to the playlist
            assert len(self.playlist_updater.video_list) == 0
        except AssertionError as e:
            self.fail(str(e))

    def test_remove_from_playlist(self):
        try:
            # Mocking the playlist content
            self.playlist_updater.playlist_listbox.insert(tk.END, "01 - Video Name - Video Director")

            # Select the item in the playlist
            self.playlist_updater.playlist_listbox.select_set(0)

            # Call remove_from_playlist
            self.playlist_updater.remove_from_playlist()

            # Assert that the playlist is empty after removal
            assert self.playlist_updater.video_list == []
            assert self.playlist_updater.playlist_listbox.size() == 0
        except AssertionError as e:
            self.fail(str(e))

    def test_play_playlist(self):
        with patch('video_library.lib.increment_play_count') as mock_increment_play_count:
            # Mocking the playlist content
            self.playlist_updater.playlist_listbox.insert(tk.END, "01 - Video Name - Video Director")

            # Call play_playlist
            self.playlist_updater.play_playlist()

            # Assert that increment_play_count is called with the correct arguments
            mock_increment_play_count.assert_called_once_with("01")


if __name__ == '__main__':
    unittest.main()

