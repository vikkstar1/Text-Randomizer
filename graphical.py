import random

class Vertex:
    def __init__(self,value):     #The initialization of the class uses a value (a word from the text) 
        self.value = value
        self.adjacent = {}        #This dictionary stores the info of the other vertices connected to this one
        self.neighbours = []
        self.neighbours_weights = []
    
    def add_edge_to(self,vertex,weight=0):
        self.adjacent[vertex] = weight      #This makes the connection between two vertices  
                                            #by storing the weight of their relationship and the name of the added vertex in the 
                                            #adjacent dictionary
    def increment_edge(self,vertex):
        self.adjacent[vertex] = self.adjacent.get(vertex, 0) + 1   #it gives its words weight if it was already encountered
        #otherwise it makes the weight equal to 1

    def get_probability_map(self):                      
        #This loop stores every vertex in a separate list from its weight  
        for (vertex,weight) in self.adjacent.items():
            self.neighbours.append(vertex)
            self.neighbours_weights.append(weight)

    def next_word(self):
        #This function returns the first element randomly chosen from the vertices by the weights
        return random.choices(self.neighbours, weights = self.neighbours_weights)[0]



class Graph:
    def __init__(self):
        self.vertices = {}       #this dictionary will map the strings to vertices in order to create Vertex objects

    def get_vertex_values(self):
        return set(self.vertices.keys())

    def add_new_vertex(self,value):

        #this function stores every word in the dictionary as a key and makes a new Vortex object with it
        self.vertices[value] = Vertex(value)

    def get_vertex(self,value):
        if value not in self.vertices:
            self.add_new_vertex(value)
        return self.vertices[value]   #This function returns the object created for some key in the dictionary

    def get_next_word(self,current_vertex):
        self.vertices[current_vertex.value].next_word()

    def create_probability_mappings(self):
        for vertex in self.vertices.values():
            vertex.get_probability_map()    