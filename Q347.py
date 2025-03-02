
import doctest

NUMBER = 0
COUNT = 1

def topKFrequent(nums, k):
    """
    FINISHED: May 19, 2024
    
    :type nums: List[int]
    :type k: int
    :rtype: List[int]

    :type nums: List[int]
    :type k: int
    :rtype: List[int]
        
    1.) Create a bucket hash table to count all integers;
    2.) Count the actual integers using the table;
    3.) Sort the integers by their counts;
    4.) Return the 'k' largest elements.

    >>> nums_1 = [1,1,1,2,2,3]
    >>> k_1 = 2
    >>> topKFrequent(nums_1, k_1)
    [1, 2]
        
    >>> nums_2 = [1]
    >>> k_2 = 1
    >>> topKFrequent(nums_2, k_2)
    [1]
    
    >>> nums_3 = [1, 2]
    >>> k_3 = 2
    >>> topKFrequent(nums_3, k_3)
    [1, 2]
    """
     # 1 - Call 'createLinkedHash' to make a hash table
    initial_table, initial_hash = createLinkedHash(nums)
    unique_num_table = []
    largest_count = 1

    # 2 - Transfer values from 'nums' into 'initial_table'
    for raw_num in nums:
        raw_hash_pos = raw_num % initial_hash
        # Empty Bucket Case Handling
        if (initial_table[raw_hash_pos] == None):
            initial_table[raw_hash_pos] = [[raw_num, 1]]  
            unique_num_table.append(raw_num)
        # Non-Empty Bucket
        else:
            existing_entry = False
            for entry in (initial_table[raw_hash_pos]):
                if entry[NUMBER] == raw_num:
                    # Match found
                    entry[COUNT] += 1
                    if (entry[COUNT] > largest_count):
                        largest_count = entry[COUNT]                    
                    existing_entry = True
                    break
            #  Match was not found
            if not existing_entry:
                initial_table[raw_hash_pos].append([raw_num, 1])
                unique_num_table.append(raw_num)

    # 3 - Sort "unique_num_table" into "sorted_count_list" by "COUNT"
    sorted_count_list = [None] * (largest_count+1) # 1 based indexing
    for unique_num in unique_num_table:
        # Find COUNT for each unique_num
        raw_hash_pos = unique_num % initial_hash
        for entry in (initial_table[raw_hash_pos]):
            if unique_num == entry[NUMBER]:
                # The unique_num has been found, now sort it in
                unique_count = entry[COUNT]
                if sorted_count_list[unique_count] is None:
                    sorted_count_list[unique_count] = [unique_num]
                else:
                    sorted_count_list[unique_count].append(unique_num)
                break
     
    # 4 - Now return the "k" largest elements from "unique_num_table"
    k_array = []
    search_index = largest_count
    while (k > 0):
        if sorted_count_list[search_index] != None:
            for each_num in sorted_count_list[search_index]:
                k_array.append(each_num)
                k -= 1
        search_index -= 1
    return k_array
    
def createLinkedHash (nums):
    """
    INPUT: unsorted list of repeating numbers
    OUTPUT: "count_table" (sized list[None]), "hash_size" (int)
    
    Helper function for topKFrequent. Creates a linked hash table. (#1)
    """
    list_cutoff = [4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 3072, 4096, 
                   5120, 6144, 7168, 8192, 9216, 10240, 20480, 30720, 40960,
                   51200, 61440, 71680, 81920, 92160, 100001]
    prime_val = [1, 3, 7, 11, 23, 43, 89, 173, 347, 683, 1031, 1367, 1709, 
                 2053, 2393, 2731, 3079, 3413, 6827, 10243, 13669, 17077, 
                 20483, 23899, 27329, 30727, 33343]
    nums_len = len(nums)
    index = 0
    while (nums_len > list_cutoff[index]):
        index += 1
    hash_size = prime_val[index]
    count_table = [None] * hash_size        
    return count_table, hash_size
        
doctest.testmod()