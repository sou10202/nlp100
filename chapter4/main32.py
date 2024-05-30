from main30 import load_mecab
import csv

def pickup_verbbase(mecab_list):
    result = []
    for line in mecab_list:
        for phrase in line:
            if phrase['pos'] == '動詞':
                result.append(phrase['base'])
    return (result)

def main():
    path = 'src/neko.txt'
    mecab_list = load_mecab(path)
    result = pickup_verbbase(mecab_list)
    with open('out/verb_base.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        for i in result:
            writer.writerow([i])

if __name__ == '__main__':
    main()