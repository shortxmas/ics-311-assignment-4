# This class is meant for task #4 of the assignment

class Tourism:
    def __init__(self, graph, tourist, start_island):
        self.graph = graph  # The graph representing the islands and connections
        self.tourist = tourist  # The tourist object
        self.start_island = start_island  # The starting island for the tour
        self.visited_islands = set()  # Set to keep track of visited islands
        self.total_time = 0  # Total travel time

    # Greedy algorithm to find next Island
    def find_next_island(self, current_island):
        next_island = None  # The next island to visit
        min_travel_time = float('inf')  # Initialize to infinity

        # Find the closest unvisited island
        for island_name, travel_time in current_island.connections.items():
            if island_name not in self.visited_islands and travel_time < min_travel_time:
                next_island = self.graph.islands[island_name]
                min_travel_time = travel_time

        return next_island, min_travel_time

    def tour(self):
        current_island = self.graph.islands[self.start_island]  # Start at the initial island
        self.visited_islands.add(current_island.name)  # Mark the starting island as visited

        while True:
            next_island, travel_time = self.find_next_island(current_island)
            if not next_island:
                break  # Exit if no unvisited islands are left

            self.visited_islands.add(next_island.name)  # Mark the island as visited
            self.total_time += travel_time  # Add travel time
            current_island = next_island  # Move to the next island

        return self.visited_islands, self.total_time  # Return the visited islands and total travel time
