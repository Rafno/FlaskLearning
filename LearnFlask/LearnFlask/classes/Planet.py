class Planet:
    """description of class"""
    def __init__(self, name ='', size=0):
        self.name = name
        self.size = size

    def introduction(self):
        return "Hello, I am the planet " + self.name + " and I weigh " + str(self.size)

    def set_name(self, name):
        self.name = name

    def set_size(self, size):
        self.size = size