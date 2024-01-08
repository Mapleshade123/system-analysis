from pandas import read_csv
import sys
import numpy as np

def task(var):
    try:
        df = read_csv(var)
        matrix = np.array(df)
        n = matrix.shape[0]
        total_entropy = 0.0
        for row in matrix:
            prob = row / (n - 1)
            prob = prob[prob != 0]
            entropy = -np.sum(prob * np.log2(prob))
            total_entropy += entropy
        return total_entropy
    except Exception as e:
        print(f"Ошибка: {str(e)}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Укажите путь к файлу")
    else:
        csv_file_path = sys.argv[1]
        print(task(csv_file_path))
