import re

def pickup_categoryname(path):
    with open(path, 'r') as f:
        text = f.read()
    result = re.findall(r'\[\[Category:(.+?)\]\]', text)
    return (result)

def main():
    result = pickup_categoryname('src/ingland.txt')
    for i in result:
        print(i)

if __name__ == '__main__':
    main()