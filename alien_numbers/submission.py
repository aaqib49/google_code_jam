from solution import run

# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Kickstart problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
  num, source, target = [str(s) for s in input().split(" ")]  # read a list of integers, 3 in this case
  target_str = run(num, source, target)
  print("Case #{}: {}".format(i, target_str))
  # check out .format's specification for more formatting options