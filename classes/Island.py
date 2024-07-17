class Island:
    def __init__(self, name, population, resources):
        self.name = name
        self.population = population
        self.resources = resources
        self.connections = {}  # Dictionary for connections {destination_island: travel_time}
