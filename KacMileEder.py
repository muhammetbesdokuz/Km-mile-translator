#ask the user to enter a km value, convert the user entered km to miles.

ConversionRate= 0.62 
km= int(input("how much km's?"))

mile= km * ConversionRate
print(str(km)+"km="+str(mile)+" miles")