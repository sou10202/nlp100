# def count_col(path, header_names):
#     import pandas as pd
#     dataset = pd.read_table(path, header=None, names=header_names)
#     return (dataset.shape[0])

# def main():
#     header_names = ["name", "sex", "Number", "year"]
#     print(count_col("src/popular-names.txt", header_names))

def count_col(path):
    with open(path, 'r') as f:
        count = sum(1 for line in f)
    return (count)

def main():
    count = count_col('src/popular-names.txt')
    print(count)

if __name__ == "__main__":
    main()