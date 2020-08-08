"""
https://leetcode.com/problems/design-hashmap/

Python Implementation.
"""

class MyHashMap(object):
        
    def __init__(self):
        
        # Use a prime number > 200 to assist with collisions
        self.hash_key = 8353
        
        
        self.hash_table = [[] for i in range(self.hash_key)]
        

    def put(self, key, value):

        # Finding the index to where the key is located by dividing the key by the hash key
        index = key % self.hash_key
        
        # Iterate through whatever lists are at that index
        for i in xrange(len(self.hash_table[index])):
            
            # Store the key and value 
            k , v =self.hash_table[index][i]
            
            # If the key in the hash table is given
            if k == key:
                
                # Key is found, update value with new or = value
                self.hash_table[index][i]=(key,value)
                return
            
        #not found in the adjoining list
        self.hash_table[index].append((key,value))
        
        

    def get(self, key):

        # Finding the index to where the key is located by dividing the key by the hash key
        index = key % self.hash_key

        # Iterate through the list at the location of the list. If key is = a key in the list, return the value.
        for i in xrange(len(self.hash_table[index])):
            
            # Store the key and value
            k, v = self.hash_table[index][i]
            
             # If the key in the hash table is given
            if k == key:
                
                # Return value
                return v
            
        # Per specs, return -1 as the key has not been found.
        return -1
            
    def remove(self, key):

        # Finding the index to where the key is located by dividing the key by the hash key
        index = key % self.hash_key

        # Iterate through the list at the location of the list
        for i in xrange(len(self.hash_table[index])):
            
            # Store the key and value
            k,v =self.hash_table[index][i]
    
            # If the key value of the tuple is = to the lookup key,  then remove the tuple from the list.
            if k == key:
            
                # Remove tuple
                self.hash_table[index].remove((k,v))
                return
