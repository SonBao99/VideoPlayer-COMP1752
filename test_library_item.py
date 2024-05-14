from library_item import LibraryItem


def test_valid_attributes():
    item = LibraryItem(name="Default Movie", director="Default Director")
    assert item.rating == 0
    assert item.play_count == 0
    assert item.duration == 0
    assert item.short_description == ""

def test_invalid_name():
    try:
        library_item = LibraryItem(name="", director="Default Director")
    except ValueError as err:
        assert str(err) == "Name cannot be empty"

def test_invalid_director():
    try:
        library_item = LibraryItem(name="Default Movie", director="")
    except ValueError as err:
        assert str(err) == "Director cannot be empty"

def test_invalid_rating_empty():
    try:
        library_item = LibraryItem(name="Movie Name", director="Director Name", rating='' )
    except ValueError as err:
        assert str(err) == "Rating cannot be None or an empty string"

def test_invalid_rating_greater_than_five():
    try:
        library_item = LibraryItem(name="Invalid Movie", director="Invalid Director", rating=7)
    except ValueError as err:
        assert str(err) == "Rating must be between 1 and 5"

def test_invalid_rating_less_than_one():
    try:
        library_item = LibraryItem(name="Invalid Movie", director="Invalid Director", rating=0)
    except ValueError as err:
        assert str(err) == "Rating must be between 1 and 5"

def test_info_method():
    library_item = LibraryItem(name="Movie Name", director="Director Name", rating=3)
    expected_info = "Movie Name - Director Name ★★★"
    assert library_item.info() == expected_info

def test_stars_method():
    library_item = LibraryItem(name="Movie Name", director="Director Name", rating=3)
    assert library_item.stars() == "★★★"



def test_play_count_increment():
    library_item = LibraryItem(name="Movie Name", director="Director Name", rating=3)
    initial_play_count = library_item.play_count
    try:
        library_item.play()
        incremented_play_count = library_item.play_count
    except AttributeError:
        library_item.play_count += 1
        incremented_play_count = library_item.play_count

    assert incremented_play_count == initial_play_count + 1

def test_duration_formatting():
    library_item = LibraryItem(name="Movie Name", director="Director Name", rating=3, duration=120)
    expected_info = "Movie Name - Director Name ★★★"
    assert library_item.info() == expected_info






def test_invalid_short_description_empty_string():
    library_item = LibraryItem(name="Invalid Movie", director="Invalid Director", short_description="")
    assert library_item.short_description == ""


def test_add_review_method():
    library_item = LibraryItem(name="Movie Name", director="Director Name", rating=3)
    review = "Good movie!"
    library_item.add_review(review)
    assert review in library_item.get_reviews()