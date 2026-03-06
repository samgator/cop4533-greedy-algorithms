import sys

# Source used: https://www.w3schools.com/dsa/dsa_data_queues.php
def fifo(req, k):
    cache = []
    misses = 0
    for r in req:
        # if hit dont do anything
        if r in cache:
            continue
        # if miss update misses and the cache
        else:
            misses = misses+1
            # if cache isnt full you can add
            if(len(cache) < k):
                cache.append(r)
            # if cache is full, first/oldest goes out and add
            else:
                cache.pop(0)
                cache.append(r)
    return misses

def lru():
    misses = 0
    return misses

def optff():
    misses = 0
    return misses

def main():
    # input file is argument 1 i.e. "../input/example1.in"
    # output file is argument 2 i.e. "../output/example1.out"
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # read file
    with open(input_file, 'r') as f:
        k, m = map(int, f.readline().split())
        requests = list(map(int, f.readline().split()))

    # calculate misses for each algorithm
    fifo_misses = fifo(requests, k)
    lru_misses = lru(requests, k)
    optff_misses = optff(requests, k)

    # write results to output file
    with open(output_file, 'w') as f:
        f.write(f"FIFO  : {fifo_misses}\n")
        f.write(f"LRU   : {lru_misses}\n")
        f.write(f"OPTFF : {optff_misses}\n")

if __name__ == "__main__":
    main()