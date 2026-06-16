
unit = input ("Is this temperature in Celcius or Fahrenheit (C/F): ").upper()
temp = float(input("Enter the temperature: "))

if unit == "C":
    temp = round((9 * temp)/ 5+ 32, 1)
    print(f"The temprerature n Fahrenheit is: {temp}°")
elif unit == "F":
    temp = round((temp - 32) * (5/9), 1)
    print(f"The temprerature n Fahrenheit is: {temp}°")
else:
    print(f"{unit} is an invalid unit of measurement")
