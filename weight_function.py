import random

random.seed(43)

def weight_function(subsets):
    return [random.randint(1, 100) for _ in range(len(subsets))]

if __name__ == "__main__":
    datasets = [20, 200, 2000]
    for i in datasets:
        folder_name = ""
        subset_length = 0
        if i == 20:
            folder_name = f"dataset_kecil"
        elif i == 200:
            folder_name = f"dataset_sedang"
        else:
            folder_name = f"dataset_besar"
        
        with open(f'{folder_name}/subset_{i}.txt', 'r') as file:
            subset_length = sum(1 for line in file if line != "\n" and line != "")

        with open(f'{folder_name}/weight_{i}.txt', 'w') as file:
            weight = weight_function([j for j in range(1, subset_length+1)])
            file.write(" ".join([str(k) for k in weight]) + '\n')
