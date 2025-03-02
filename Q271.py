
import doctest

def encode(strs):
    """
    FINISHED: May 19, 2024
    
    This function will concatenate a list of strings into a single string.
    Strings will be broken up by three numbers, which represent the length
    and allow "decode" to work.
    
    >>> list_1 = ["neet", "code", "love", "you"]
    >>> print(encode(list_1))
    004neet004code004love003you
    
    >>> list_2 = ["we","say",":","yes"]
    >>> print(encode(list_2))
    002we003say001:003yes
    """
    encoded_string = ""
    for word in strs:
        len_to_str = str(len(word))
        word_len = len_to_str.zfill(3) # Pad int with 0's if needed: 3 digits
        encoded_string += (word_len + word)
    return encoded_string
    
def decode(s):
    """
    This function splits the above string back into base components, using
    the counts as cutoff points.
    
    >>> str_1 = "004neet004code004love003you"
    >>> print(decode(str_1))
    ['neet', 'code', 'love', 'you']
    
    >>> str_2 = "002we003say001:003yes"
    >>> print(decode(str_2))
    ['we', 'say', ':', 'yes']
    """    
    decoded_list = []
    while s != "":
        word_len = int(s[:3])
        word = s[3:(3 + word_len)]
        decoded_list.append(word)
        s = s[(3 + word_len):]
    return decoded_list
    
doctest.testmod()