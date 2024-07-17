class IslandGraph:
    def __init__(self):
        self.islands = {}

    def add_island(self, island):
        self.islands[island.name] = island

    def add_route(self, from_island, to_island, travel_time):
        if from_island in self.islands and to_island in self.islands:
            self.islands[from_island].connections[to_island] = travel_time
            self.islands[to_island].connections[from_island] = travel_time