import sys

def split_n(path, n):
    with open(path, 'r') as f:
        data = f.readlines()
    max_col = len(data)
    m = int(max_col/n)
    remaind = max_col - m * n
    for i, count in enumerate(range(0, m*n, m), 1):
        with open (f'out/split{i}.txt', 'w') as f:
            for line in data[count: count+m]:
                print(line, file=f, end="")
    if (remaind != 0):
        with open(f'out/split{n}.txt', 'a') as f:
            for line in data[-remaind ::]:
                print(line, file=f, end="")

def main():
    args = sys.argv
    path = 'src/popular-names.txt'
    if (len(args) == 1):
        n = 5
    else:
        n = int(args[1])    
    split_n(path, n)

if __name__ == "__main__":
    main()