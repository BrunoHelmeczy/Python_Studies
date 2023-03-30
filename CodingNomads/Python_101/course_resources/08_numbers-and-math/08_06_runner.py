# If a runner runs 10 miles in 30 minutes and 30 seconds,
# What is their average speed in kilometers per hour?
# (Tip: 1 mile = 1.6 km)

def convertSpeed2KmperHour(Miles = 10, Minutes = 30, Secs = 30):
    secs = 60 * Minutes + Secs
    kms = Miles * 1.6

    return kms / (secs/3600)

convertSpeed2KmperHour()