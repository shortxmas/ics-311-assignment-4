# This class is meant for task #4 of the assignment

class Tourism:
    def __init__(self, graph, tourist, start_island):
        self.graph = graph
        self.tourist = tourist
        self.start_island = start_island
        self.visited_islands = set()
        self.total_time = 0

    def find_next_island(self, current_island):
        # Find the next island with the most experiences within the shortest travel time
        next_island = None
        min_travel_time = float('inf')

        for island_name, travel_time in current_island.connections.items():
            if island_name not in self.visited_islands and travel_time < min_travel_time:
                next_island = self.graph.islands[island_name]
                min_travel_time = travel_time

        return next_island, min_travel_time

    def tour(self):
        current_island = self.graph.islands[self.start_island]
        self.visited_islands.add(current_island.name)

        while True:
            next_island, travel_time = self.find_next_island(current_island)
            if not next_island:
                break 

            self.visited_islands.add(next_island.name)
            self.total_time += travel_time
            current_island = next_island

        return self.visited_islands, self.total_time