def tab_to_space(path):
    f = open('src/popular-names.txt', 'r')
    data = f.read()
    f.close()
    data = data.replace('\t', ' ')
    return (data)

def main():
    path = 'src/popular-names.txt'
    print(tab_to_space(path))

if __name__ == "__main__":
    main()