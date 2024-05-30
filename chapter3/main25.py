import re

def extra_template(path):
    with open(path, 'r') as f:
        text = f.read()
    lines = text.split('\n')
    result = {}
    for i in lines:
        ans = re.search(r'\|(.+?)\s=\s*(.+)', i)
        if ans:
            result[ans[1]] = ans[2]
    return (result)
    
def main():
    path = 'src/ingland.txt'
    result = extra_template(path)
    for i in result:
        print(i, result[i], sep=" : ")

if __name__ == "__main__":
    main() 