# get user inputs for:
    # KMs to drive
    # litres/ km gas usage of car
    # fuel price
# return fuel costs for the trip - use string Formatting

dist = input('How far is your destination (in km) ?')
gas = input("how much gasoline does your car use in 100kms ?")
price = input("what's the current USD gas price per litre ?")

dist    = float(dist)
gas     = float(gas)
price   = float(price)

gasused = (dist/100) * gas
Price = gasused * price

print(f"You'll use {round(gasused)} litres of gas for your trip. It'll cost you in total ${round(Price, 2)}.\n")

print("ride a bike\n")