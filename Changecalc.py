print ("Let me help you add up your change!")
quartervalue = float(input ("How many quarters? ")) * 0.25
print (quartervalue)
dimevalue = float(input ("How many dimes? ")) * 0.10
print (dimevalue)
nickelvalue = float(input ("How many nickels? ")) * 0.05
print (nickelvalue)
pennyvalue = float (input ("How many pennies? ")) * 0.01
print (pennyvalue)
print (float(quartervalue + dimevalue + nickelvalue + pennyvalue))  
