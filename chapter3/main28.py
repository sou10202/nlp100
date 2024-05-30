import re
from main25 import extra_template
from main26 import del_markup
from main27 import del_link

def remove_markup(d):
    p_ref1 = re.compile('\<ref\>.+?\<\/ref\>')
    p_ref2 = re.compile('\<ref name.+?\/\>')
    p_br = re.compile('\<br \/\>')
    for i in d:
        d[i] = re.sub(p_ref1, '', d[i])
        d[i] = re.sub(p_ref2, '', d[i])
        d[i] = re.sub(p_br, '', d[i])
    return (d)

def main():
    path = 'src/ingland.txt'
    ans = extra_template(path)
    ans = del_markup(ans)
    ans = del_link(ans)
    ans = remove_markup(ans)
    for i in ans:
        print(i, ans[i], sep=" : ")

if __name__ == "__main__":
    main() 