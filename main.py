import math, random

class graph:
	def __init__(self):
		self.graph = {}
		self.vectors = []
		self.M = 16
		self.entry_point = None

	def add(self, vector):
		self.vectors.append(vector)
		node_id = len(self.vectors) - 1
		self.graph[node_id] = {}
		max_layer = int(-math.log(random.random()) * (1 / math.log(self.M)))
		for layer in range(max_layer + 1):
			self.graph[node_id][layer] = []

def main():
    g = graph()
    for i in range(50):
        g.add([random.random(), random.random(), random.random()])
    
    for node_id, layers in g.graph.items():
        max_l = max(layers.keys())
        if max_l > 0:
            print(f"Node {node_id}: max layer {max_l}")
    
    print(f"\nTotal nodes: {len(g.vectors)}")
    
if __name__ == "__main__":
    main()