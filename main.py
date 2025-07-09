import math

mainCubeDimensions = int(input("Enter the mainCubeDimensions of the hypercube: "))
verticies = 2**mainCubeDimensions
edges = mainCubeDimensions * 2**(mainCubeDimensions-1)
squares = math.comb(mainCubeDimensions, 2) * (2 ** (mainCubeDimensions - 2))

print("------------------------------------------------------------------------------")
print(f"General stats for the {mainCubeDimensions}D cube:")
print(f"Verticies: {verticies}")
print(f"Edges: {edges}")
print(f"Squares: {squares}")

# Show how many n-1;n-2;n-3...n-x cubes are in an n-dimensional cube
# Show how many x-1 dimensional cubes are in an x-dimensional cube
amountOfTotalCubes = 1
for x in range(mainCubeDimensions, 0, -1):
    numOfSubcubes = 2 * x
    print("------------------------------------------------------------------------------")
    print(f"A {x}-dimensional cube consists of {numOfSubcubes} {x-1}-dimensional cubes.")
    print(f"A {mainCubeDimensions}-dimensional cube has {amountOfTotalCubes} {x}-dimensional cubes.")
    amountOfTotalCubes *= numOfSubcubes

print("------------------------------------------------------------------------------")
