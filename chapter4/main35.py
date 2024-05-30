from main30 import load_mecab
import collections, csv

def count_words(mecab_list):
    count_list = []
    for line in mecab_list:
        for word in line:
            if (word['pos'] != '補助記号'):
                count_list.append(word['surface'])
    c = collections.Counter(count_list)
    return (c.most_common())

def main():
    path = 'src/neko.txt'
    mecab_list = load_mecab(path)
    c = count_words(mecab_list)
    with open('out/word_count.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['word', 'count'])
        writer.writerows(c)

if __name__ == '__main__':
    main()