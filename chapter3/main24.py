import re

def extra_file(path):
    with open(path, 'r') as f:
        text = f.read()
    result = re.findall(r'\[\[ファイル:(.+?)\|.*\]\]', text)
    print(result)

def main():
    path = 'src/ingland.txt'
    extra_file(path)

if __name__ == "__main__":
    main()

# def extract_files(text):
#     text = text.split('\n')
#     ans = []
#     for line in text:
#         i = 7
#         if line[0:7] == '[[ファイル:':
#             while (line[i] != '|'):
#                 i += 1
#             ans.append(line[7:i])
#     return (ans)

# def main():
#     path = 'src/jawiki-country.json'
#     db = json_db(path)
#     text = extract_keywords(db, 'イギリス')
#     ans = extract_files(text)
#     print(ans)