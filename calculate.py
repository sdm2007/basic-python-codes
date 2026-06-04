n1=int(input(("Enter number 1:")))
n2=int(input(("Enter number 2:")))

op=input(("which operation you want to perform? enter 1 for addition 2 for substractions 3 for multiplication 4 for division:"))
if op=="1":
    add=n1+n2
    result=add
    print("your answer is",result)
elif op=="2":
    sub=n1-n2
    result=sub
    print("your answer is",result)
elif op=="3":
    multi=n1*n2
    result=multi
    print("your answer is",result)
elif op=="4":
    if n2==0:
        print("error division by zero not applicable")
    else:
        div=n1/n2
        result=div
        print("your answer is",result)

