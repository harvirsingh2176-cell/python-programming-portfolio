# Importing Decimal
from decimal import Decimal, InvalidOperation

# Setting Up Temperature Asking F(x)
def ask_value(value):
    # keep asking until user enters a number
    while True:
        try:
            temp_value=Decimal(input("Temperature: "))
            return temp_value
        except InvalidOperation:
            print("This is not a number\nTry again")

# Asking unit to change
temp_unit= input("Unit to change: ").strip().lower()

# Fahrenheit Condition (Convert to Fahrenheit)
if(temp_unit == "fahrenheit"):
    fahrenheit=(((ask_value("Frahenheit"))-32)/9)*5
    print(f"{fahrenheit:.2f} °C")

# Celsius Condition (Convert to Celsius)
elif(temp_unit == "celsius"):
    celsius=(((ask_value("Celsius"))*9)/5)+32
    print(f"{celsius:.2f} °F")

else:
    print("Unknown Unit")

print("Thank You")