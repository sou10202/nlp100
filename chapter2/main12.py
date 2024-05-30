from main11 import tab_to_space

def pullout_n(data, n):
    lines = data.split("\n")
    del lines[-1] # 最後の行にある改行が一つ余分になっているので省く
    for i in range(len(lines)):
        lines[i] = lines[i].split(" ") # linesの要素をさらに単語ごとに分割する
    with open(f'out/col{n}.txt', 'w') as f:
        for i in lines:
            print(i[n - 1], sep='\n', file=f)
    
def main():
    data = tab_to_space('src/popular-names.txt')
    pullout_n(data, 1)
    pullout_n(data, 2)

if __name__ == "__main__":
    main()