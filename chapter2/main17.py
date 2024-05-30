from main11 import tab_to_space

def unique_n(data, n):
    lines = data.split("\n")
    del lines[-1] # 最後の行にある改行が一つ余分になっているので省く
    for i in range(len(lines)):
        lines[i] = lines[i].split(" ") # linesの要素をさらに単語ごとに分割する
    unilist = []
    for i in lines:
        unilist.append(i[n - 1])
    unilist = set(unilist)
    unilist = list(unilist)
    unilist.sort()
    return (unilist)

def main():
    data = tab_to_space('src/popular-names.txt')
    uniset = unique_n(data, 1)
    for i in uniset:
        print(i, sep='\n')

if __name__ == "__main__":
    main()