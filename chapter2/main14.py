import sys

def head_n(path, n):
    with open(path, 'r') as f:
        data = f.read().split('\n')
    del data[-1]
    for i in range(n):
        print(data[i])

def main():
    args = sys.argv
    path = 'src/popular-names.txt'
    if (len(args) == 1):
        n = 5
    else:
        n = int(args[1])
    head_n(path, n)

if __name__ == "__main__":
    main()