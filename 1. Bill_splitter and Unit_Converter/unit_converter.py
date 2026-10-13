distance = float(input("Enter the distance : "))
unit = input("Enter the unit that the you have km or mile : ")
if unit == "km":
    print(round((distance*0.621371),2))
else:
    print(round((distance*1.60934),2))
