#
# Syafiera
# Pandas practice
#

import pandas as pd

# Load data
df2 = pd.read_csv("diabetes.csv")

# Add missing value
df2 = df2.copy()
df2.loc[2:5, 'Pregnancies'] = None
df2.head(10)