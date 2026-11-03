# Calculator

# Symbols Used
list={
    "Sum": "+",
    "Difference":"-",
    "Product":"*",
    "Exponent":"^",
    "Quoitent":"/",
    "root":"root",
    "Percent":"%"
}

print(list)

# Asking for numbers
a=int(input("Number1: "))
b=int(input("NUmber2: "))

# Asking of Operation
operation=str(input("Operation: "))

# Calculator Logic
if(operation=="+"):
    print("Sum: ",a+b)
elif(operation=="-"):
    print("Difference: ",a-b)
elif(operation=="*"):
    print("Product: ",a*b)
elif(operation=="^"):
    print("Square: ",a**b)
elif(operation=="/"):
    print("Quoitent: ",a/b)
elif(operation=="root"):
    print("Sqrt: ",a**(1/b))
elif(operation=="%"):
    print("Percent:",(a/b)*100)
else:
    print("Check operation List")

print("Thank You")