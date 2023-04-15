import pandas as pd
from pathlib import Path

# 1) read in Salaries.csv --> sal
filename = next(Path.cwd().rglob('Salaries.csv'))
sal = pd.read_csv(filename, index_col = 'Id')

# 2-3) Check head() / info() / describe() / shape
sal.head()
sal.info()
sal.describe()
sal.shape

# 4) Avg base pay
# sal.columns
sal['BasePay'].mean()

# 5) max overtime pay
# sal.columns
sal['OvertimePay'].max()

# 6) job title of JOSEPH DRISCOLL
sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['JobTitle']

# 7) how much does joseph driscoll earn ?
sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['TotalPayBenefits']

# 8) name of highest paid person ?
sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].max()]['EmployeeName']

# 9) name of lowest paid person ?
sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].min()]['EmployeeName']
# +1: negative 'OtherPay'

# 10) mean BasePay per year 
sal.groupby('Year')[['BasePay']].mean()

# 11) count() unique job titles
len(sal['JobTitle'].unique())

# 12) top 5 most common job
sal['JobTitle'].count()

sal.groupby('JobTitle').count()['EmployeeName'].sort_values(
    ascending = False
).head(5)

# 13) nr job titles only once in 2013
a13_1 = sal[sal['Year'] == 2013].groupby('JobTitle').count()['EmployeeName']
a13 = a13_1[a13_1 == 1].count()

# 14) nr pax w 'Chief' in their job title ?
sal[sal['JobTitle'].str.contains('Chief')].shape[0]
sal[sal['JobTitle'].str.lower().str.contains('chief')].shape[0]

# 15) correlation of job title string length & totalPayBenefits
sal2 = sal.copy()[['JobTitle', 'TotalPayBenefits']]
sal2['JobTitleLen'] = sal2['JobTitle'].str.len()

sal2.corr()
sal2['TotalPayBenefits'].corr(sal2['JobTitleLen'])