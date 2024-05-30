import re

def pickup_category(path):
    with open(path, 'r') as f:
        text = f.read()
    result = re.findall(r'\[\[Category:.+?\]\]', text)
    return (result)

def main():
    result = pickup_category('src/ingland.txt')
    for i in result:
        print(i)

if __name__ == '__main__':
    main()
