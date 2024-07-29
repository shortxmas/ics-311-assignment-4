# This class is for task #2 of the assignment
import queue
import math

class ResourcePlanting:
    def __init__(self, graph, resource, source_island):
        self.graph = graph
        self.resource = resource
        self.source_island = source_island{"color":"w", "distance":float('inf'), "parent":None}

    def plant(self):
        # Plant resources implementation
    	per_island = int(math.floor(self.resource.get()/len(self.graph)))
	    counter = self.resource.get()

	    for x in (self.graph.islands - self.source_island):
		    setattr(x,"color","w")
		    setattr(x,"distance",float('inf'))
		    setattr(x,"parent",None)

	    self.source_island.color = "g"
	    self.source_island.distance = 0
	    qq = queue.Queue(maxsize=len(self.graph))
	    qq.put(self.source_island)
	
	    while qq.qsize() != 0:
		    x = qq.get()			
		    for y in self.graph[x]:
			    if y.color == "w":
				    y.color = "g"
				    y.distance = x.distance + 1
				    y.parent = x
				    qq.put(y)
		    x.color = "b"
		    print("Delivering resources to the visited island…")
		    counter = counter - per_island
		    x[resource] = x[resource] + per_island
		    print("\nResources delivered!")

	    endtxt = f"All islands have been visited and received the resource. There were {counter} units of supply leftover."
	    print(endtxt)    
