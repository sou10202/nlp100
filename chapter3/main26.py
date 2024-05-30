import re
from main25 import extra_template

def del_markup(d):
    for i in d:
        d[i] = re.sub(r'\'\'+', '', d[i])
    return(d)

def main():
    path = 'src/ingland.txt'
    ans = extra_template(path)
    result = del_markup(ans)
    for i in result:
        print(i, result[i], sep=" : ")


if __name__ == '__main__':
    main()