class individual():
    def __init__(self,latitude,longitude,stories,elevation,square_feet,basement,total_market_value):
        self.latitude = latitude
        self.longitude = longitude
        self.stories = stories
        self.elevation = elevation
        self.square_feet = square_feet
        self.basement = basement
        self.total_market_value = total_market_value

    def decide_to_relocate(self):
        return True

