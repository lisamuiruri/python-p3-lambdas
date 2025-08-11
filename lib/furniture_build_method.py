class Furniture:
    def build(self):
        print("Your furniture is being built")

class Table(Furniture):
    def build(self):
        print("You have chosen a table")
        super().build()

# Example usage
if __name__ == "__main__":
    print("Creating regular furniture:")
    chair = Furniture()
    chair.build() # Calls Furniture's build method

    print("\nCreating a table:")
    dining_table = Table()
    dining_table.build() # Calls Tbale's build method which extends Furniture's