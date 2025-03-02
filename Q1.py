
import doctest

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    
    >>> nums_1 = [2, 7, 11, 15]
    >>> target_1 = 9
    >>> print (twoSum(nums_1, target_1))
    [0, 1]
    
    >>> nums_2 = [3, 2, 4]
    >>> target_2 = 6
    >>> print (twoSum(nums_2, target_2))
    [1, 2]
    
    >>> nums_3 = [3, 3]
    >>> target_3 = 6
    >>> print (twoSum(nums_3, target_3))
    [0, 1]
    
    """

    # 1 - Pick a size for the hash table
    list_len = [4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 3072, 4096, 
                5120, 6144, 7168, 8192, 9216, 10001]
    prime_val = [7, 17, 37, 67, 131, 257, 521, 1031, 2053, 4099, 6151, 
                8209, 10243, 12289, 14341, 16411, 18433, 19997]
    input_size = len(nums)
    index = 0
    while (list_len[index] < input_size):
        index += 1
    hash_size = prime_val[index]
        
    # 2 - Create and populate the table
    two_sum_hash = hash_size * [None]
    for index, candidate in enumerate(nums):
        probe = 0
        position_found = False
        while not position_found:
            hash_position = (candidate + probe**2) % hash_size
            if two_sum_hash[hash_position] is None:
                two_sum_hash[hash_position] = [candidate, index]
                position_found = True
            else:
                probe += 1
    
    # 3 - Find the two sum via the hash table
    for index, candidate in enumerate(nums):
        partner = target - candidate
        probe = 0
        candidate_checked = False
        while not candidate_checked:
            hash_position = (partner + probe**2) % hash_size
            if (two_sum_hash[hash_position] is None):
                candidate_checked = True
            elif (two_sum_hash[hash_position][0] == partner and 
                  two_sum_hash[hash_position][1] != index):
                return [index, two_sum_hash[hash_position][1]]
            else:
                probe += 1
        
doctest.testmod()