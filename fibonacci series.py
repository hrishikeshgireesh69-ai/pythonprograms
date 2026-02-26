def fib(n):
 a,b=0,1
 for i in range(n):
  print(a,end=" ")
  a,b=b,a+b

invalid=0
while 1:
 print("\n1 fib\n2 exit")
 ch=input("choice: ")
 if ch=="1":
  try:
   n=int(input("enter terms: "))
   if n<=0: raise ValueError
   fib(n)
  except:
   print("wrong input")
   invalid+=1
 elif ch=="2":
  print("ended\nwrong entries:",invalid)
  break
 else:
  print("wrong choice")
  invalid+=1
