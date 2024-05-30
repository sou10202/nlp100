from main11 import tab_to_space

def sort_col(data):
    data = data.split('\n')
    del data[-1]
    for i in range(len(data)):
        data[i] = data[i].split(' ')
    return(sorted(data, key=lambda x: int(x[2])))

def main():
    path = 'src/popular-names.txt'
    data = tab_to_space(path)
    sorted_data = sort_col(data)
    for i in sorted_data:
        print()
        for j in i:
            print(j, end=" ")

if __name__ == "__main__":
    main()