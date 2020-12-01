num_list = []
num_file = open("numList.txt", "r")
for line in num_file:
  num_list.append(int(line.rstrip("\n")))
for num1 in num_list:
  for num2 in num_list:
    for num3 in num_list:
      new_num = num1 + num2 + num3
      if new_num == 2020:
        print(num1 * num2 * num3)
