from main30 import load_mecab
import csv


def artic(mecab_list):
    result = []
    for line in mecab_list:
        nouns = ''
        count = 0
        for i in range(len(line)):
            if line[i]['pos'] == '名詞':
                nouns += line[i]['surface']
                count += 1
            else:
                if count > 1:
                    result.append(nouns)
                count = 0
                nouns = ''
    return (set(result))
        
def main():
    path = 'src/neko.txt'
    mecab_list = load_mecab(path)
    result = artic(mecab_list)
    with open('out/co_noun.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        for i in result:
            writer.writerow([i])

if __name__ == '__main__':
    main()