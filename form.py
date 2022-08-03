import random
import string
from graphical import Graph, Vertex


def get_word_from_text(text_path):
    with open(text_path, 'r') as f:
        text = f.read()

        text = ' '.join(text.split())                                       #skips pages
        text = text.lower() 
        text = text.translate(str.maketrans('','',string.punctuation))      #skips punctuation

    words = text.split()                                                    #divides the text through spaces
    return words 

def make_graph(words):
    g = Graph()
    previous_word = None
    for word in words:
        word_vertex = g.get_vertex(word)
        if previous_word:                                   
            previous_word.increment_edge(word_vertex)                   

        previous_word = word_vertex

    g.create_probability_mappings()
    return g          

def compose(g, words,length=50):
    random_text = []
    word = g.get_vertex(random.choice(words))           #chooses a random start
    for _ in range(length):
        random_text.append(word.value)
        word = g.get_next_word(word)

    return random_text


def main():
    words = get_word_from_text('./texts/eminem.txt')        #sets words for all the separated words from a text 
    g = make_graph(words)
    random_text = compose(g,words,100)
    return ' '.join(random_text)

if __name__ == '__main__':
    print(main())    