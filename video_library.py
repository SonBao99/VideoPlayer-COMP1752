from library_item import LibraryItem


library = {}
library["01"] = LibraryItem("Tom and Jerry", "Fred Quimby", 4, 94, "Join the timeless adventures of the iconic cat and mouse duo, Tom and Jerry. Filled with laughter and mischief, their classic antics make this animated series a family favorite.")
library["02"] = LibraryItem("Breakfast at Tiffany's", "Blake Edwards", 5, 106, "Immerse yourself in the glamorous world of New York City as Audrey Hepburn stars in Breakfast at Tiffanys. Follow Holly Golightly captivating journey of love and self-discovery.")
library["03"] = LibraryItem("Casablanca", "Michael Curtiz", 2, 102, "Step into the intrigue of wartime Casablanca, where love and politics collide. Humphrey Bogart and Ingrid Bergman's timeless performances make this film a cinematic masterpiece.")
library["04"] = LibraryItem("The Sound of Music", "Robert Wise", 1, 175, "Embark on a musical adventure with the von Trapp family in the Austrian Alps. The Sound of Music weaves a heartwarming tale of love, music, and resilience.")
library["05"] = LibraryItem("Gone with the Wind", "Victor Fleming", 3, 238, "Set against the backdrop of the American Civil War, Gone with the Wind is an epic romance that follows the fiery Scarlett O'Hara. Witness the sweeping saga of love and survival.")


def list_all(): #a function whose main perpose is to list all the videos in the library
    output = ""
    for key in library:
        item = library[key]
        output += f"{key} {item.info()}\n"
    return output


def get_name(key):
    try:
        item = library[key]
        return item.name
    except KeyError:
        return None
    
def get_duration(key):
    try:
        item = library[key]
        return item.duration
    except KeyError:
        return -1

def get_short_description(key):
    try:
        item = library[key]
        return item.short_description
    except KeyError:
        return None


def get_director(key):
    try:
        item = library[key]
        return item.director
    except KeyError:
        return None


def get_rating(key):
    try:
        item = library[key]
        return item.rating
    except KeyError:
        return -1


def set_rating(key, rating):
    try:
        item = library[key]
        item.rating = rating
    except KeyError:
        return


def get_play_count(key):
    try:
        item = library[key]
        return item.play_count
    except KeyError:
        return -1


def increment_play_count(key):
    try:
        item = library[key]
        item.play_count += 1
    except KeyError:
        return

def add_review(video_number, new_review):
    if video_number in library:
        library[video_number].add_review(new_review)
    else:
        print(f"Video {video_number} not found in the library")

def get_reviews(key):
    try:
        item = library[key]
        return item.reviews
    except KeyError:
        return []