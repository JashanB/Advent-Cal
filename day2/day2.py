input_file = open("input.txt", "r")
total_correct = 0
for line in input_file:
  count = 0
  full_text = line.split(':')
  query_string = full_text[1].rstrip("\n")
  key_char = full_text[0].split(' ')[1]
  num1 = int(full_text[0].split('-')[0])
  num2 = int(full_text[0].split('-')[1].split(' ')[0])
  for char in query_string:
    if char == key_char:
      count += 1
  if count >= num1 and count <= num2:
    total_correct += 1
  # print(key_char)
  # print(query_string)
  # print(full_text)
  # print(num1)
  # print(num2)
print(total_correct)