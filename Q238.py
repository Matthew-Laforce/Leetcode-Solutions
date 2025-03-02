
import doctest

def productExceptSelf(nums):
        """
        FINISHED: May 21, 2024
        
        >>> nums_1 = [1, 2, 3, 4]
        >>> print(productExceptSelf(nums_1))
        [24, 12, 8, 6]
        
        >>> nums_2 = [-1, 1, 0, -3, 3]
        >>> print(productExceptSelf(nums_2))
        [0, 0, 9, 0, 0]
        
        Iterate through nums twice, once in each direction, to get the products
        of everything to the left and to the right of each integer in the 
        array.
        """
        item_count = len(nums)
        result = [1] * item_count       # Multiplicative identity
        
        # Multiply from left to right
        k = 0
        mult_product = 1
        while k < (item_count - 1):
                mult_product *= nums[k]
                result[k+1] *= mult_product
                k += 1
        
        # Multiply right to left
        mult_product = 1
        while k > 0:
                mult_product *= nums[k]
                result[k-1] *= mult_product
                k -= 1

        return result

doctest.testmod()