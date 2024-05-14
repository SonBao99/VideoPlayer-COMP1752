
class CheckingMenu:
    def __init__(self, id, name, price, quantity):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = 0
        self.items_in_cart = []
        self.items_in_wishlist = []

    def show_menu(self):
        print (f'Menu shown here: {self.id}, {self.name}, {self.price}, {self.quantity}')
        print (f'1. Add to cart')
        print (f'2. Add to wishlist')
        print (f'3. Back to main menu')

    def populate_menu(self):
        print(f'Populating menu here: {self.id}, {self.name}, {self.price}, {self.quantity}')

    def add_to_wishlist(self):
        input = int(input('Enter item number: '))
        self.items_in_wishlist.append(input)
        print (f'Items in wishlist: {self.items_in_wishlist}')

    def add_to_cart(self):
        input = int(input('Enter item number: '))
        self.items_in_cart.append(input)
        print (f'Items in cart: {self.items_in_cart}')

    def back_to_menu(self):
        pass


    def add_review(self):
        if review in reviews:
            msb.showinfo("Success", "Review already exists")
        else:
            reviews.append(review)
            msb.showinfo("Success", "Review added")


        