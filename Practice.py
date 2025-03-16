a = int(input("Enter the number"))

num = a

if num<50:
  print("The number is less then fifty", num)
  if num>25:
    print("The number is greater than twenty five", num)
  else:
    print("The number is less than twenty five", num)
    if num%2==0:
      print("This number is even")
    else:
      print("the number is odd")  
else:
  print("This number is greater than fifty", num)
    
    
    