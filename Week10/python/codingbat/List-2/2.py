def sum67(nums):
  ok = True
  cnt = 0
  for i in range(len(nums)):
    if ok and nums[i]!=6:
      cnt+=nums[i]
    elif nums[i]==6:
      ok = False
    elif nums[i]==7 and ok == False:
      ok =True
  return cnt