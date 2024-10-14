class Graph(object):
    
    def __init__(self, size):
        # Initialize the adjacency matrix with all zeros
        self.adjMatrix = []
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
        # Set the size of the matrix
        self.size = size

    # Add a vertex to the graph
    def add_vertex(self):
        # Add a new row and column of zeros to the matrix
        self.adjMatrix.append([0] * (self.size + 1))
        for i in range(self.size):
            self.adjMatrix[i].append(0)
        # Increase the size of the matrix
        self.size += 1

    # Add an edge to the graph
    def add_edge(self, v1, v2):
        # Check that the vertices are within the bounds of the matrix
        if v1 >= 0 and v1 < self.size and v2 >= 0 and v2 < self.size:
            # Check that the edge doesn't already exist
            if self.adjMatrix[v1][v2] == 0 and self.adjMatrix[v2][v1] == 0:
                # Add the edge to the matrix
                self.adjMatrix[v1][v2] = 1
                self.adjMatrix[v2][v1] = 1

    # Remove an edge from the graph
    def remove_edge(self, v1, v2):
        # Check that the vertices are within the bounds of the matrix
        if v1 >= 0 and v1 < self.size and v2 >= 0 and v2 < self.size:
            # Check that the edge exists
            if self.adjMatrix[v1][v2] == 1 and self.adjMatrix[v2][v1] == 1:
                # Remove the edge from the matrix
                self.adjMatrix[v1][v2] = 0
                self.adjMatrix[v2][v1] = 0

    # Print the graph as a matrix
    def print_matrix(self):
        # Print the column headers
        print(" ", end="")
        for i in range(self.size):
            print(" ", i+1, end="")
        print()
        # Print the row headers and matrix values
        for i in range(self.size):
            print(i+1, end="")
            for j in range(self.size):
                print(" ", self.adjMatrix[i][j], end="")
            print()

# Example usage
def main():
    # Create a new graph with 6 vertices
    g = Graph(6)
    # Add a new vertex
    g.add_vertex()
    # Add edges between vertices
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    # Print the matrix representation of the graph
    g.print_matrix()
    # Remove an edge from the graph
    g.remove_edge(2, 3)
    # Print the updated matrix representation of the graph
    g.print_matrix()

if __name__ == '__main__':
   main()
