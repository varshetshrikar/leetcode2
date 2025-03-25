class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

       
        number_map = {}

       
        for i, num in enumerate(nums):
            
            diff = target - num

          
            if diff in number_map:
                
                return [number_map[diff], i]

           
            number_map[num] = i
       
        return None
