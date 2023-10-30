class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        pre_sum = [0]
        for num in nums:
            pre_sum.append(pre_sum[-1]+num)
        
      
        inc_stack = []
        min_len = len(nums)+1

        for pre in range(len(pre_sum)):
            while inc_stack and pre_sum[inc_stack[-1]]>pre_sum[pre]:
                inc_stack.pop()
                
            inc_stack.append(pre)
            
            while (pre_sum[pre]-pre_sum[inc_stack[0]])>=k:
                min_len = min(min_len,pre-inc_stack.pop(0))
              
            
        return -1 if min_len==len(nums)+1 else min_len
                