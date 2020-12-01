num_list = []
num_file = open("numList.txt", "r")
for line in num_file:
  num_list.append(int(line.rstrip("\n")))
for num, index in enumerate(num_list):
  