class Person:
    def __init__(self, name):
        self.name = name
        
    def talk(self):
        print(f"Hello I am {self.name}, how are you today?")

john = Person("John")
john.talk()