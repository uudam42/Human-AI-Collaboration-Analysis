"""" Project :The Impact of AI Adoption, Revenue Increase, and AI-Generated Content on
    Human-AI Collaboration Across Countries"""

#import tools
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm

#read data from csv file
df = pd.read_csv("ai_data.csv")

#select relative variable
df = df[['AI Adoption Rate (%)','AI-Generated Content Volume (TBs per year)',
         'Revenue Increase Due to AI (%)',
         'Human-AI Collaboration Rate (%)']]

#clean data
df = df.dropna()

#data review and basic statistics
print("Cleaned Data Preview:")
print(df.head())
print('\nStatistical Description')
print(df.describe())

#create heat map on a 14 x 8 canvas
plt.figure(figsize=(14,8))
sns.heatmap(df.corr(),annot=True,cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()


#independant variable
X = df[['AI Adoption Rate (%)','AI-Generated Content Volume (TBs per year)',
         'Revenue Increase Due to AI (%)']]

#dependant variable
Y = df['Human-AI Collaboration Rate (%)']

#intercept
X = sm.add_constant(X)

#running regression analysis and output result
Model = sm.OLS(Y,X).fit()
print("\nRegression Result:")
print(Model.summary())

#create scatter plot
sns.pairplot(df)
plt.suptitle("Scatterplot of Key Variables",y=1.02)
plt.show()
