# 担当
import re
from main25 import extra_template
from main26 import del_markup

def del_link(d):
    link = re.compile(r'\[\[(?!ファイル:)(.+?)\]\]')
    for i in d:
        d[i] = re.sub(link, '\\1', d[i])
    return (d)

def main():
    path = 'src/ingland.txt'
    ans = extra_template(path)
    ans = del_markup(ans)
    ans = del_link(ans)
    for i in ans:
        print(i, ans[i], sep=" : ")

if __name__ == "__main__":
    main()