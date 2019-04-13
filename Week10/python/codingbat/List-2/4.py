def centered_average(nums):
  nums.sort()
  cnt = 0
  m  = 0
  for i in range(1,len(nums)-1):
    cnt+=nums[i]
    m+=1
  return cnt/m
