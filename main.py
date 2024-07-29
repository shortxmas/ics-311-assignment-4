from classes.Island import Island
from classes.IslandGraph import IslandGraph
from classes.Tourism import Tourism
from classes.ResourcePlanting import ResourcePlanting

def task4Main():
    # Create islands
    island_a = Island(name="A", population=100, resources={"food": 50, "water": 100}, )
    island_b = Island(name="B", population=50, resources={"wood": 200, "kahelelani shells": 30})
    island_c = Island(name="C", population=70, resources={"sweet potatoes": 150, "kalo": 100})

    # Create a graph and add islands
    graph = IslandGraph()
    graph.add_island(island_a)
    graph.add_island(island_b)
    graph.add_island(island_c)

    # Add routes between islands
    graph.add_route("A", "B", 10)
    graph.add_route("A", "C", 20)
    graph.add_route("B", "C", 15)

    # Initialize tourism algorithm
    tourism = Tourism(graph=graph, tourist="John Doe", start_island="A")
    visited_islands, total_time = tourism.tour()

    print(f"Visited islands: {visited_islands}")
    print(f"Total travel time: {total_time}")

    # Initialize resource planting algorithm
    distribution = ResourcePlanting(graph=graph, resource="kahelelani shells", source_island="B")
    distribution.plant()

def main():
    task4Main()
    
main()
