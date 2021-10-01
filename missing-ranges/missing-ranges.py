class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        result = []
        nums.append(upper+1)
        prev_num = lower - 1
        for num in nums:
            # Base case if num in nums is lower than the LOWER given:
            if num < lower: 
                continue

            # 2nd Base case if there is a num thats inbetween two nums:
            if min(num, upper+1) == prev_num + 2:
                result.append(str(prev_num+1))

            # 3rd base case where there is a gap greater than two from the num and prev num
            elif min(num, upper+1) > prev_num + 2:
                result.append(str(prev_num + 1) + "->" + str(min(num, upper+1)-1))
            if num >= upper: break
            prev_num = num
        return result