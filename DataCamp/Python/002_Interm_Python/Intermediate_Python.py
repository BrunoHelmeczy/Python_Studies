import pandas as pd
gapminder = pd.read_csv('https://assets.datacamp.com/production/repositories/287/datasets/5b1e4356f9fa5b5ce32e9bd2b75c777284819cca/gapminder.csv')
cars = pd.read_csv('https://assets.datacamp.com/production/repositories/287/datasets/79b3c22c47a2f45a800c62cae39035ff2ea4e609/cars.csv')
BRICS = pd.read_csv('https://assets.datacamp.com/production/repositories/287/datasets/b60fb5bdbeb4e4ab0545c485d351e6ff5428a155/brics.csv')


# 1) Matplotlib -----
    # pip3 install ipykernel
import matplotlib.pyplot as plt

year = [1950, 1970, 1990, 2010]
pop = [2.5, 3.69, 5.26, 6.97]

plt.plot(year, pop)
plt.show()
    # Change keyboard shortcuts: File > Preferences > Keyboard Shortcuts
    # Have python plots in VSCode pop-up window ?

plt.scatter(year, pop)
plt.show()

gapminder.columns[-1]
gapminder.columns[-2]

gapminder['life_exp']
gapminder['gdp_cap']

plt.scatter(gapminder['gdp_cap'], gapminder['life_exp'])
plt.xscale('log') # accepted values: log, linear, symlog, logit, function, functionlog
plt.show()

plt.scatter(gapminder['population'], gapminder['life_exp'])
plt.show()



# 1.1 ) Histograms ----
# help(plt.hist)

plt.hist(gapminder['life_exp'], bins = 20, cumulative=True, density=True)
plt.show()

# help(plt.clf) --> plt.clf() --> Clean Figure

# 1.2) Customizations ----
plt.scatter(x = gapminder['gdp_cap'], y = gapminder['life_exp'])
plt.xscale('log')
plt.xlabel('GDP per Capita (log-scale)')
plt.ylabel('Life Expectancy')
plt.title('Country GDPs vs Life Expectancy')
plt.ylim(bottom = 0)

xtick_val = list(range(0, gdpMax, int(gdpMax/5) ))
xtick_lab = [str(int(x/1000)) + str('K $') for x in xtick_val ]
plt.xticks(xtick_val, xtick_lab)
plt.xlim(left = 0)

plt.show()

cols = list(['red', 'green', 'blue', 'yellow', 'black'])
gapminder['cont'].unique()

mycols = dict(zip(*list([list(gapminder['cont'].unique()), cols])))


plt.scatter(
    x = gapminder['gdp_cap'], 
    y = gapminder['life_exp']
    , s = gapminder['population']/1000000
    , c = [mycols[cont] for cont in gapminder['cont']]
    , alpha = 0.5
)
plt.xscale('log')
plt.text(10000, 50, 'What a lovely plot')
plt.grid(True)
plt.show()




# 2) Dictionaries & Pandas -----

# 3) Logic, Ctrl Flows & Filtering -----

# 4) Loops -----

# 5) Case study ----

