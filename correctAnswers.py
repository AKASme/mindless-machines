# This is simply to count the amount of questions GPT got right.
c = open("GPT (MMLU).txt")
e = 0
for i in c:
  if "True" in i:
    e += 1

print(e)
