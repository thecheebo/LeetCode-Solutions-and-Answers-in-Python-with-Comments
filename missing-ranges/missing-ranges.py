class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        result = []
        nums.append(upper+1)
        pre = lower - 1
        for i in nums:
            if i < lower: continue
            if min(i, upper+1) == pre + 2:
                result.append(str(pre+1))
            elif min(i, upper+1) > pre + 2:
                result.append(str(pre + 1) + "->" + str(min(i, upper+1)-1))
            if i >= upper: break
            pre = i
        return result