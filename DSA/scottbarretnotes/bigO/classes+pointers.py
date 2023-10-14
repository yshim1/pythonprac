#Classes

class Cookie:
    def __init__(self, color):  #Because this init takes self as a parameter, it is a method not a function. Methods are associated w classes/objects
        self.color = color
    
    def set_color(self, color):
        self.color = color
        
    def get_color(self):
        return self.color
    
green_cookie = Cookie('green')

"""
Self keyword means that it is a class method and not a function
"""