def sum2(nums):
  cnt = 0 
  x = min(len(nums),2)
  for i in range(x):
    cnt+=nums[i]
  return cnt
