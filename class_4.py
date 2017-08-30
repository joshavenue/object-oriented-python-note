class RaceCar:
    laps=0                                                      // This is an ATTRIBUTE
    def __init__(self, color, fuel_remaining, **kwargs):        // This is a method
        self.color = color
        self.fuel_remaining = fuel_remaining

        for key, value in kwargs.items():
            setattr(self, key, value)

    def run_lap(self, length):
        self.fuel_remaining -= (length * .125)
        self.laps += 1
