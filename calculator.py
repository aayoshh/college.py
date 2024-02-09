x=int(input("Enter the first number=\t"))
y=int(input("Enter second number=\t"))

def addition():
    a=x+y
    print("Sum of two numbers is=\t",a)

def substraction():
    s=x-y
    print ("Diffrence of two number is=\t",a)

def multiplication():
    m=x*y
    print("product of two numbers is=\t",m)

def division():
    if y==0:
        print("division is not possible.")        
    else:
        d=float(x)/float(y)
        print("solution for division is=\t",d)
print_fun ={"+":addition,"-":substraction,"*":multiplication,"/":division}
print_xo=str(input("choose operator example(+,-,*,/)\t"))
answer=print_fun.get(print_xo)
answer()
