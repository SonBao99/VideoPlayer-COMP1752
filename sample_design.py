class SampleDesign():

    def __init__(self, id, name, type):
        self.id  = id
        self.name = name
        self.type = type 

    def show_menu(self):
        print(f'Menu should be here!: ')
        print(f'1. test1')
        self.choose_function()


    def choose_function(self):
        while True:
            print('Menu choosing user')
            if self.choose_function() == None:


