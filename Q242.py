
import doctest

def isAnagram(s, t):
    """
    FINISHED: April 29, 2024
    
    :type s: str
    :type t: str
    :rtype: bool
    
    This function determines whether two strings of lower-case letters are
    anagrams or not. 
    
    >>> print (isAnagram("anagram", "nagaram"))
    True
    >>> print (isAnagram("rat", "car"))
    False
    """
    # If lengths do not match, or the words are the same: NOT anagrams!
    if (len(s) != len (t)) or (s == t):
        return False
    
    # Else, count the letters in each word by placing them into arrays.
    s_array = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for index in s:
        position = (ord(index) - 96)
        s_array[position]+=1
    t_array = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]  
    for index in t:
        position = (ord(index) - 96)
        t_array[position]+=1
        
    # Then return the equality value. 
    return (s_array == t_array)

doctest.testmod()