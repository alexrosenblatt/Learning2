file_name = 'pi_million_digits.txt'

with open(file_name) as file_object:
  lines = file_object.readlines()

pi_string = ''
for line in lines:
  pi_string += line.strip()

birthday = input("enter your birthday")
if birthday in pi_string:
  print("yes!")
else:
  print("no")

