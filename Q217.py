
# Finished December 14, 2023

class Solution(object):
    def containsDuplicate(self, nums):
        
        # Given an array "nums", return False if no dupes are found, else True.
        
        # Size an appropriate hash table for the length of 'nums'        
        array_size = len(nums)  
        if array_size == 0:
            return False
        elif array_size < 10:
            hasher = 23
        elif array_size < 100:
            hasher = 251
        elif array_size < 1000:
            hasher = 2503
        elif array_size < 10000:
            hasher = 25013
        else:
            hasher = 250007
        hash_table = [None] * hasher
            
        # Create a loop to handle the items within 'nums'
        index = 0
        while index < array_size:
            
            # Find the hash table position for the newest value
            position = (nums[index] % hasher)
            
            # In the easy case, the position is empty...
            if hash_table[position] == None:
                hash_table[position] = nums[index]
                
            # Perhaps instead the position is not empty
            else: 
                probe = 1
                position_found = False
                
                # Duplicates, or collision? 
                while position_found == False:
                    
                    position = ((nums[index] + probe**2) % hasher)
                    
                    # Suppose collision, which has since been managed...
                    if hash_table[position] == None:
                        hash_table[position] = nums[index]
                        position_found = True
                        
                    # Suppose unmanaged collision
                    elif hash_table[position] != nums[index]:
                        probe += 1
                        
                    # Otherwise, a duplicate has been found, return True
                    else:
                        return True

                # With each possibility handled, increment index and keep going
                index += 1
            
        # Suppose no duplicates are found... then reset table, return False
        hash_table = [None] * hasher
        return False