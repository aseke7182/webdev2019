def make_chocolate(small, big, goal):
  goal -= min(goal/5*5,big * 5)
  if goal > small:
    return -1
  return goal
