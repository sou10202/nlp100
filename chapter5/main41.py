from main40 import Morph

class Chunk:
    def __init__(self, morphs, dst):
        self.morphs = morphs
        self.dst = dst
        self.srcs = []

def div_chunks():
    morphs = []
    sentences = []
    chunks = []
    with open('src/ai.ja.txt.parsed', 'r') as f:
        for line in f:
            if line.startswith('*'):
                if len(morphs):
                    chunks.append(Chunk(morphs, dst))
                morphs = []
                dst = int(line.split(' ')[2].rstrip('D'))
            elif line != 'EOS\n':
                morphs.append(Morph(line))
            else:
                if len(morphs):
                    chunks.append(Chunk(morphs, dst))
                morphs = []
                if len(chunks):
                    for i, chunk in enumerate(chunks):
                        dst = chunk.dst
                        if dst == -1:
                            continue
                        chunks[dst].srcs.append(i)
                    sentences.append(chunks)
                chunks = []
    return sentences

def main():
    sentences = div_chunks()
    for chunk in sentences[1]:
        print(vars(chunk))

if __name__ == '__main__':
    main()