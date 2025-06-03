import math

dimensions = int(input("Enter the dimensions of the hypercube: "))
verticies = 2**dimensions
edges = dimensions * 2**(dimensions-1)
squares = math.comb(dimensions, 2) * (2 ** (dimensions - 2))

print(f"The hypercube has {verticies} verticies, {edges} edges, and {squares} squares.")
