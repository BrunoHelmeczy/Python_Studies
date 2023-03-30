# Exercise Link: https://github.com/CodingNomads/python_miniprojects/tree/master/population_growth

def getYearInSeconds():
    return 60 * 60 * 24 * 365

def getFuturePopulation(PopNow = 380123456, YearsAhead = 3, BirthSecs = 6, DeathSecs = 12, MigrSecs = 40):
    timeleft = YearsAhead * getYearInSeconds()

    Deaths = timeleft / DeathSecs
    Births = timeleft / BirthSecs
    Migrat = timeleft / MigrSecs

    return max([0, int(PopNow + Births - Deaths - Migrat)])

getFuturePopulation()
