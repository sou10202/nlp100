from main41 import div_chunks
from graphviz import Digraph

def plot_tree(sentence):
    g = Digraph(format='png', filename='out44')
    g.attr('node')
    for chunk in sentence:
        if chunk.dst == 1:
            continue
        word_to = ''.join([x.surface if x.pos != '記号' else '' for x in chunk.morphs])
        word_by = ''.join([x.surface if x.pos != '記号' else '' for x in sentence[chunk.dst].morphs])
        g.edge(word_to, word_by)
    g.view()

def main():
    sentences = div_chunks()
    plot_tree(sentences[1])

if __name__ == '__main__':
    main()