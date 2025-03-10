
import doctest

def groupAnagrams(strs):
        """
        FINISHED: May 1, 2024
        
        :type strs: List[str]
        :rtype: List[List[str]]
        
        1.) Create a dynamically sized hash table to hold all the values from 
            strs (O(n)).
        2.) Convert each word from "strs" into [[count of sorted letters], 
            [index]].
        3.) Hash using the [count of sorted letters] (O(n)). Two collision 
            handling cases: if they do not match, use quadratic probing; if 
            they do, append [index] with the new value (O(n))
        4.) Erase all empty cases from the array; convert all indices back to 
            original strings (O(n)); return the new array.
        
        Overall runtime O(n)
        
        >>> strs_1 = ["eat","tea","tan","ate","nat","bat"]
        >>> print (groupAnagrams(strs_1))
        [['eat', 'tea', 'ate'], ['bat'], ['tan', 'nat']]
        
        >>> strs_2 = [""]
        >>> print (groupAnagrams(strs_2))
        [['']]
        
        >>> strs_3 = ["a"]
        >>> print (groupAnagrams(strs_3))
        [['a']]
        """
        
        # 1 - Pick a size for the hash table; generate empty table
        list_len = [4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 3072, 4096, 
                    5120, 6144, 7168, 8192, 9216, 10001]
        prime_val = [7, 17, 37, 67, 131, 257, 521, 1031, 2053, 4099, 6151, 
                    8209, 10243, 12289, 14341, 16411, 18433, 19997]
        input_size = len(strs)
        index = 0
        while (list_len[index] < input_size):
            index += 1
        hash_size = prime_val[index]
        hash_table = hash_size * [None]
        
        # 2 - Convert values into [[count of sorted letters], [index]]        
        for index, word in enumerate(strs):
                new_word_num = 0
                for letter in word:
                        letter_to_num = ord(letter) - 97
                        new_word_num += 1*10**(letter_to_num * 3)
                
                # 3 - Add 'new_entry' into the hash table
                probe = 0
                position_found = False
                while not position_found:
                        hash_position = (new_word_num + probe**2) % hash_size
                        if (hash_table[hash_position] == None):
                                new_entry = [[new_word_num], [index]]
                                hash_table[hash_position] = new_entry
                                position_found = True
                        elif (hash_table[hash_position][0][0] == new_word_num):
                                hash_table[hash_position][1].append(index)
                                position_found = True
                        else:
                                probe += 1
                
        # 4 - Clean up "hash_table", converting back to words; return it
        anagram_array = []
        for item in hash_table:
                if (item != None):
                        new_word_group = []
                        for index in item[1]:
                                new_word_group.append(strs[index])
                        anagram_array.append(new_word_group)
        return anagram_array

doctest.testmod()
