def concat1_2(path1, path2):
    f1 = open(path1, 'r')
    f2 = open(path2, 'r')

    data1 = f1.read().split('\n')
    data2 = f2.read().split('\n')
    del data1[-1]
    del data2[-1]

    f1.close()
    f2.close()

    with open('out/concat1_2.txt', 'w') as f:
        for i in range(len(data1)):
            print(data1[i],data2[i], sep='\t', file=f)
    return ()

def main():
    path1 = "out/col1.txt"
    path2 = "out/col2.txt"
    concat1_2(path1, path2)

if __name__ == "__main__":
    main()