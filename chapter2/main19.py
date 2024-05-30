from main17 import unique_n
from main11 import tab_to_space

def mode_rate(data):
    unilist = unique_n(data, 1)
    data = data.split('\n')
    modelist = []
    for i in range(len(data)):
        data[i] = data[i].split(' ')
    for uni in unilist:
        count = 0
        for i in range(len(data)):
            if data[i][0] == uni:
                count += 1
        modelist.append((uni, count))
    modelist = sorted(modelist, key=lambda x: int(x[1]))
    return (modelist)

def main():
    path = 'src/popular-names.txt'
    data = tab_to_space(path)
    print(data)
    modelist = mode_rate(data)
    for i in modelist:
        print(i[0])

if __name__ == "__main__":
    main()