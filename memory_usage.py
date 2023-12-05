import tracemalloc
from greedy_weighted_set_cover import set_cover
from branch_and_bound_weighted_set_cover import BB

def memory_usage_greedy_weighted_set_cover(universes, subsets, weights, datasets):
    print("-------------GREEDY MEMORY USAGE--------------")
    for i in range(len(datasets)):
        print(f"-----------------DATASET {datasets[i]}----------------")
        tracemalloc.start()
        result = set_cover(universes[i], subsets[i], weights[i])
        memory = tracemalloc.get_traced_memory()
        cover, weight = result[0], result[1]
        print("weight:", weight)
        print(f"memory_usage: {memory}")
        print()

def memory_usage_branch_and_bound_weighted_set_cover(universes, subsets, weights, datasets):
    print("-------------B&B MEMORY USAGE--------------")
    for i in range(len(datasets)):
        print(f"-----------------DATASET {datasets[i]}----------------")
        tracemalloc.start()
        result = BB(universes[i], subsets[i], weights[i])
        memory = tracemalloc.get_traced_memory()
        weight, temp_cover = result[0], result[1]
        print("weight:", weight)
        print(f"memory usage: {memory}")
        print()

def generate_input(datasets):
    universes = [0, 0, 0]
    subsets = [[], [], []]
    weights = [0, 0, 0]

    # generate universes
    for i in range(len(datasets)):
        folder_name = ""
        if i == 0:
            folder_name = f"dataset_kecil"
        elif i == 1:
            folder_name = f"dataset_sedang"
        else:
            folder_name = f"dataset_besar"
        with open(f"{folder_name}/universe_{datasets[i]}.txt", 'r') as file:
            for line in file:
                line = line.strip().strip("\n")
                if line == "":
                    break
                universes[i] = set([int(j) for j in line.split(" ")])

    # generate subsets
    for i in range(len(datasets)):
        folder_name = ""
        if i == 0:
            folder_name = f"dataset_kecil"
        elif i == 1:
            folder_name = f"dataset_sedang"
        else:
            folder_name = f"dataset_besar"
        with open(f"{folder_name}/subset_{datasets[i]}.txt", 'r') as file:
            for line in file:
                line = line.strip().strip("\n")
                if line == "":
                    break
                subsets[i].append(set([int(j) for j in line.split(" ")]))
    
    # generate weights
    for i in range(len(datasets)):
        folder_name = ""
        if i == 0:
            folder_name = f"dataset_kecil"
        elif i == 1:
            folder_name = f"dataset_sedang"
        else:
            folder_name = f"dataset_besar"
        with open(f"{folder_name}/weight_{datasets[i]}.txt", 'r') as file:
            for line in file:
                line = line.strip().strip("\n")
                if line == "":
                    break
                weights[i] = [int (j) for j in line.split(" ")]

    return universes, subsets, weights

if __name__ == "__main__":
    datasets = [20, 200, 2000]
    universes, subsets, weights = generate_input(datasets)
    memory_usage_greedy_weighted_set_cover(universes, subsets, weights, datasets)
    memory_usage_branch_and_bound_weighted_set_cover(universes, subsets, weights, datasets)
