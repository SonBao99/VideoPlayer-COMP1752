import unittest
from library_item import LibraryItem
from video_library import *

class TestVideoLibrary(unittest.TestCase):
    def test_list_all(self):
        expected_output = "01 Tom and Jerry - Fred Quimby ★★★\n02 Breakfast at Tiffany's - Blake Edwards ★★★★★\n"
        assert list_all() == expected_output

    def test_get_name(self):
        assert get_name("01") == "Tom and Jerry"
        # assert get_name("03") is None  # Video not found

    def test_get_duration(self):
        assert get_duration("02") == 106
        # assert get_duration("03") == -1  # Video not found

    def test_get_short_description(self):
        assert get_short_description("01") == "Join the timeless adventures of the iconic cat and mouse duo, Tom and Jerry. Filled with laughter and mischief, their classic antics make this animated series a family favorite."
        # assert get_short_description("03") is None  # Video not found

    def test_get_director(self):
        assert get_director("02") == "Blake Edwards"
        # assert get_director("03") is None  # Video not found

    def test_get_rating(self):
        assert get_rating("01") == 4
        assert get_rating("03") == -1  # Video not found

    def test_set_rating(self):
        set_rating("01", 5)
        assert get_rating("01") == 5
        set_rating("03", 3)  # Video not found, no change

    def test_get_play_count(self):
        assert get_play_count("02") == 0
        assert get_play_count("03") == -1  # Video not found

    def test_increment_play_count(self):
        increment_play_count("02")
        assert get_play_count("02") == 1
        increment_play_count("03")  # Video not found, no change

    def test_add_review(self):
        add_review("02", "Beautiful cinematography.")
        assert "Beautiful cinematography." in get_reviews("02")
        add_review("03", "New review")  # Video not found, no change
        assert get_reviews("03") == []

    def test_get_reviews(self):
        assert get_reviews("01") == ["Great classic cartoons!", "Tom and Jerry never gets old.", "Awesome animation!"]
        # assert get_reviews("03") == []  # Video not found

if __name__ == '__main__':
    unittest.main()