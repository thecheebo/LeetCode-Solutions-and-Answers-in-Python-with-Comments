'''
https://leetcode.com/problems/next-permutation/

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1


'''

class Solution:
    def nextPermutation(self, nums):
        
        # Length of array
        n = len(nums)
        
        # Iterate through the index starting at the end 
        for i in range(n-1, 0, -1):
            
            # If a number before it is less than
            if nums[i] > nums[i-1]:
                
                #make a copy of the current index
                j = i
                
                # Finding Pivot Point
                while j < n and nums[j] > nums[i-1]:
                    
                    # idx will save what the last pivot point is
                    idx = j
                    
                    j += 1
               
                # swap the number at the pivot point with each number prior to the pivot point to the end
                nums[idx], nums[i-1] = nums[i-1], nums[idx]
                
                
                # swap the rest of the numbers at the pivot point from the start
                for k in range((n-i)//2):
                    
                    nums[i+k], nums[n-1-k] = nums[n-1-k], nums[i+k]
                    
                break
        
        # If the entire is is in descending order, reverse the list
        else:
            nums.reverse()
