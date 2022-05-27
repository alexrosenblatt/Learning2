filename = 'responses2.txt'

while True:
  with open(filename,'a') as file_object: 
    file_object.write(input(f"Why do you like programming?"))
  file_object.close()