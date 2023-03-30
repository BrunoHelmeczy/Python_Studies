# Take in the following three values from the user:
# 1. investment amount
# 2. annual interest rate in percentage
# 3. number of years to invest
#
# Calculate the future values and print them to the console.
# implement monthly savings added

def calcInvFutureValue(amount = 15000, returnrate = 0.06, monthlysavings = 1000, years2invest = 5):
    principal = round(amount * ((1 + returnrate) ** years2invest))

    months2invest = years2invest * 12
    monthlyraturn = returnrate/12

    savings = sum([monthlysavings * ( (1 + monthlyraturn) ** x) for x in range(1, months2invest+1)])

    return round(principal + savings)

# calcInvFutureValue(15000, 0.06, 1000, 5)
# calcInvFutureValue(15000, 0.06, 1500, 5)
# calcInvFutureValue(15000, 0.06, 1500, 10)
# calcInvFutureValue(15000, 0.06, 1500, 15)
# calcInvFutureValue(15000, 0.06, 1500, 20)
# calcInvFutureValue(15000, 0.1, 1500, 25)
