class LibraryItem:
    def __init__(self, name, director, rating=0, duration=0, short_description=""):
        if rating is None or rating == '':
            raise ValueError("Rating cannot be None or an empty string")

        try:
            rating = int(rating)
            if rating < 1 or rating > 5:
                raise ValueError("Rating must be between 1 and 5")
        except ValueError as e:
            # This block will only execute if the conversion to int fails,
            # and it will not catch the initial None or empty string check
            print(f"Error: {e}")
            rating = 0

        
        self.name = name
        self.director = director
        self.rating = rating
        self.play_count = 0
        self.duration = duration
        self.short_description = short_description
        self.reviews = []

    def info(self):
        return f"{self.name} - {self.director} {self.stars()}"

    def stars(self): 
        stars = ""
        for i in range(self.rating):
            stars += "★"
        return stars


    def add_review(self, new_review):
        self.reviews.append(new_review)

    def get_reviews(self):
        return self.reviews
    

