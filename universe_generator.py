
def universe_generator(size):
    return [i for i in range(1, size + 1)]

if __name__ == "__main__":
    datasets = [20, 200, 2000]
    for i in datasets:
        folder_name = ""
        if i == 20:
            folder_name = f"dataset_kecil"
        elif i == 200:
            folder_name = f"dataset_sedang"
        else:
            folder_name = f"dataset_besar"
        with open(f"{folder_name}/universe_{i}.txt", 'w') as file:
            universe = universe_generator(i)
            file.write(" ".join([str(j) for j in universe]))