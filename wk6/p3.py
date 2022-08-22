def happy():

  input_string = input("String: ")

  if len(input_string) == 1:

     print("Happy? False")

  if input_string[0] == "g" and input_string[1] != "g":

     print("Happy? False")

  if input_string[-1] == "g" and input_string[-2] != "g":

     print("Happy? False")

  else:

     print("Happy? True")

happy()