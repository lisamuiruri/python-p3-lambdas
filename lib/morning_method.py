class DailyRoutine:
    def morning(sekf):
        print("coffee")
        print("shower")

class MondayRoutine(DailyRoutine):
    def morning(self):
        print("jog") # New functionality (added before parent's method)
        super().morning() # Calls parent's morning() (coffee + shower)
        