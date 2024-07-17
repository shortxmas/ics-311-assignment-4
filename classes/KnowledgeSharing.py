import heapq

class KnowledgeSharing:
    def __init__(self, graph, populations, leader, start_island):
        """
        Initialize the KnowledgeSharing class.

        :param graph: Dictionary where keys are islands and values are lists of tuples (neighboring_island, travel_time)
        :param populations: Dictionary where keys are islands and values are population sizes
        :param leader: The leader sharing knowledge
        :param start_island: The starting island for the leader
        """
        self.graph = graph
        self.populations = populations
        self.leader = leader
        self.start_island = start_island
        self.visits = {island: float('inf') for island in graph}  # Tracks last visit time to each island

    def share_knowledge(self):
        """
        Share knowledge across the sea of islands.
        """
        pq = [(0, self.start_island)]  # (time, island)
        self.visits[self.start_island] = 0

        while pq:
            current_time, current_island = heapq.heappop(pq)

            for neighbor, travel_time in self.graph[current_island]:
                new_time = current_time + travel_time

                # Prioritize islands with higher populations and more recent visits
                if new_time < self.visits[neighbor]:
                    self.visits[neighbor] = new_time
                    heapq.heappush(pq, (new_time, neighbor))
                    print(f"Leader visited {neighbor} from {current_island} at time {new_time}")

        print("Knowledge sharing completed.")
        print("Visit times:")
        for island, time in self.visits.items():
            print(f"{island}: {time}")

if __name__ == "__main__":
    # Example graph (island, travel_time) format
    graph = {
        'Hawaii': [('Tahiti', 5), ('Fiji', 8)],
        'Tahiti': [('Hawaii', 5), ('Fiji', 3), ('Samoa', 2)],
        'Fiji': [('Hawaii', 8), ('Tahiti', 3), ('Samoa', 6)],
        'Samoa': [('Tahiti', 2), ('Fiji', 6)],
    }

    populations = {
        'Hawaii': 1000,
        'Tahiti': 800,
        'Fiji': 600,
        'Samoa': 400,
    }

    leader = 'Chief Navigator'
    start_island = 'Hawaii'

    sharer = KnowledgeSharing(graph, populations, leader, start_island)
    sharer.share_knowledge()
