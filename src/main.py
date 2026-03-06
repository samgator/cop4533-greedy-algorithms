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

# Source used: https://www.geeksforgeeks.org/computer-organization-architecture/cache-replacement-policies/
# and https://www.geeksforgeeks.org/system-design/lru-cache-implementation/
def lru(req, k):
    cache = []
    misses = 0
    for r in req:
        # if hit remove current item spot and add it back so its in the most recently used spot
        if r in cache:
            cache.remove(r)
            cache.append(r)
        # if miss update misses and the cache
        else:
            misses = misses+1
            # if cache isnt full you can add
            if(len(cache) < k):
                cache.append(r)
            # if cache is full the least recently used gets popped and the newest item gets added to the end (most recently used spot)
            else:
                cache.pop(0)
                cache.append(r)
    return misses

# source: https://www.geeksforgeeks.org/operating-systems/beladys-anomaly-in-page-replacement-algorithms/
def optff(req, k):

    cache = []
    misses = 0

    for r in req:
        # if hit, do nothing
        if r in cache:
            continue
        # if miss, update misses and the cache
        else:
            misses += 1
            # if cache isnt full, add
            if(len(cache) < k):
                cache.append(r)
            # if cache is full, find the item that will be used furthest in the future, pop it, then add new item
            else:
                furthest_index = -1
                furthest_item = None
                # loop through cache and find the item that will be used furthest in the future
                for item in cache:
                    # if item is not in future requests, then it is the furthest item so break loop
                    if item not in req[req.index(r):]:
                        furthest_item = item
                        break
                    # if item in the future requests, find the index of the next time it will be used and compare to furthest index found so far
                    else:
                        index = req[req.index(r):].index(item)
                        if index > furthest_index:
                            furthest_index = index
                            furthest_item = item

                cache.remove(furthest_item)
                cache.append(r)

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