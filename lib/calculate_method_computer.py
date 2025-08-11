class Computer:
    def __init__(self, name, ram, hd):
        self.name = name
        self.ram_amount = ram
        self.hd_amount = hd

    def calculate(self):
        return "Crunching numbers!"
    
class Laptop(Computer):
    def calculate(self): # Overrides Computer.calculate()
        return "Processing mathematics!"
    
if __name__ == "__main__":
    #Create object computer
    desktop = Computer("Desktop", 16, 512)
    print(desktop.calculate()) #Output: "Crunching numbers!"

    #Create a laptop object (inherits from computer)
    notebook = Laptop("Notebook", 8, 256)
    print(notebook.caluclate()) #Output: "Processing mathematics!"