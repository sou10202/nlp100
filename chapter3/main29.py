import re, requests
from main25 import extra_template
from main26 import del_markup
from main27 import del_link
from main28 import remove_markup

path = 'src/ingland.txt'
ans = extra_template(path)
ans = del_markup(ans)
ans = del_link(ans)
ans = remove_markup(ans)

s = requests.Session()

url = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "format": "json",
    "titles": "File:" + ans['国旗画像'],
    "prop": "imageinfo",
    "iiprop" : "url"
}

R = s.get(url=url, params=PARAMS)
DATA = R.json()
PAGES = DATA['query']['pages']
for k, v in PAGES.items():
    print(v['imageinfo'][0]['url'])