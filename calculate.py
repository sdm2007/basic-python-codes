add=n1+n2
sub=n1-n2
multi=n1*n2
div=n1/n2
n1=input(print("Enter number 1:"))
n2-input(print("Enter number 2:"))

op=input(print("which operation you want to perform? enter 1 for addition 2 for substractions 3 for multiplication 4 for division:"))
if op==1:
  result=input(add)
if op==2:
   result=input(sub)
if op==3:
   result=input(multi)
if op==4:
  if n2==0:
    print("error")
  else:
    result=input(div)
print("your answer is", result)
