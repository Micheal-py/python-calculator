print("choose your option to ")
print("1,addition")
print("2,subtraction")
print("3,division")
print("4,multiplication")

choice = input("Choice: ")

if (int(choice) == 1):
  num1 = input("Enter the first num: ")
  num2 = input("Enter the second num: ")
  result = int(num1) + int(num2)
  print("result: " + str(result))
  
elif (int(choice) == 2):
  num1 = input("Enter the first num: ")
  num2 = input("Enter the second num: ")
  result = int(num1) - int(num2)
  print("result: " + str(result))
elif (int(choice) == 3 ):
  num1 = input("Enter the first num: ")
  num2 = input("Enter the second num: ")
  result = int(num1) / int(num2)
  print("result: " + str(result))
elif (int(choice) == 4 ):
  num1 = input("Enter the first num: ")
  num2 = input("Enter the second num: ")
  result = int(num1) * int(num2)
  print("result: " + str(result))
