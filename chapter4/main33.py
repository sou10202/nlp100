from main30 import load_mecab
import csv

def pickup_noun(mecab_list):
    result = []
    for line in mecab_list:
        for i in range(len(line)):
            if line[i]['surface'] == 'の':
                if (line[i-1]['pos'] == '名詞') and (line[i+1]['pos'] == '名詞'):
                    result.append(line[i-1]['surface']+'の'+line[i+1]['surface'])
    return (result)
                
def main():
    path = 'src/neko.txt'
    mecab_list = load_mecab(path)
    result = pickup_noun(mecab_list)
    with open('out/noun.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        for i in result:
            writer.writerow([i])

if __name__ == '__main__':
    main()