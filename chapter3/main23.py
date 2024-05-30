import re
from main20 import json_db, extract_keywords

def extract_section(path):
    with open(path, 'r') as f:
        text = f.read()
    result = re.findall(r'(==+)\s*(.+?)\s*==+', text) # ==の後にスペースがある時のない時があったので\sで省けるようにした
    return (result)

def main():
    path = 'src/ingland.txt'
    result = extract_section(path)
    for i in result:
        print(f'{i[1]} : Lv.{len(i[0])}')

if __name__ == "__main__":
    main()
