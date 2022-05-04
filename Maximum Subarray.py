      def maxSubArray(self, nums: List[int]) -> int:
        
        s = 0
        maxsub = nums[0] 
        
        for i in range(len(nums)):
            if s < 0:
                s = 0 #don't consider that element and any element before it hence making s = 0
            s+= nums[i]
            maxsub = max(maxsub, s)
            
        return maxsub
