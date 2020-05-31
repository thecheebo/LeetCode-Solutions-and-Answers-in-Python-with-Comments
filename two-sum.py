class Solution(object):
    def twoSum(self, nums, target):
        
        # Create an empty dictionary
        d = {}
   
        # Iterate through Array with an Indexable Value
        for i, n in enumerate(nums):
            
            # Get the value you are matching target
            m = target - n
            
            # Search if its in the dictionary
            if m in d:
                return [i, d[m]]
            
            # If it isn't then add this value with the current key with the index as its value
            else:
                d[n] = i
