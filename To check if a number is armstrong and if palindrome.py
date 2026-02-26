def getnum():
 try:
  return int(input("enter number: "))
 except:
  return None

def pal(n):
 r=0
 t=n
 while t>0:
  r=r*10+t%10
  t=t//10
 return r==n

def arm(n):
 s=str(n)
 c=len(s)
 t=n
 tot=0
 while t>0:
  d=t%10
  tot=tot+d**c
  t=t//10
 return tot==n

invalid=0
while True:
 print("1 palindrome")
 print("2 armstrong")
 print("3 exit program")
 ch=input("choice: ")

 if ch=="1" or ch=="2":
  num=getnum()
  if num==None:
   print("wrong input")
   invalid+=1
  else:
   if ch=="1":
    print("palindrome" if pal(num) else "not palindrome")
   else:
    print("armstrong" if arm(num) else "not armstrong")

 elif ch=="3":
  print("program ended")
  print("wrong entries:",invalid)
  break

 else:
  print("wrong choice")
  invalid+=1
