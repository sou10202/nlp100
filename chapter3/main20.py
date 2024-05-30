import json

def json_db(path):
    db = []
    with open(path) as f:
        for line in f:
            db.append(json.loads(line))
    return (db)

def extract_keywords(db, words):
    for i in db:
        if i['title'] == words:
            return(i['text'])
    return ()

def main():
    path = 'src/jawiki-country.json'
    db = json_db(path)
    print(extract_keywords(db, ('イギリス')))


if __name__ == "__main__":
    main()