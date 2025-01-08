import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib as mt
import seaborn as sb

df=pd.read_csv("C:/Users/PRAJWAL/OneDrive/Desktop/Data Analysis/Expanded_data_with_more_features.csv")
print(df.head(5))


print(df.drop,"unnamed=0")
print(df.head)


# GENDER DISTRIBUTION
plt.figure(figsize=(5,4))
plt.title("gender distribution")
ax=sb.countplot(data=df,x="Gender")
ax.bar_label(ax.containers[0])
plt.show()

# FROM THE ABOVE CHART WE HAVE ANALYZED THAT :
# The no. of female in the data is more than no. of males.
        

# IMPACT OF PARENTS EDUCATION ON STUDENTS SCORE

gp=df.groupby("ParentEduc").agg({'MathScore':'mean','ReadingScore':'mean'})
print(gp)

#IN THE HEAT MAP
plt.figure(figsize=(8, 6))
sb.heatmap(gp, annot=True, fmt=".2f", cmap="coolwarm")
plt.title("Impact of Parent Education on Student Scores")
plt.xlabel("Score Type")
plt.ylabel("Parent Education Level")
plt.show()

# From the above chart we got to know that the education of parents had the good impact on the students score

# ETHNIC GROUP DISTRIBUTION

print(df['EthnicGroup'].unique())

groupA=df.loc[(df['EthnicGroup']=="group A")].count()
groupB=df.loc[(df['EthnicGroup']=="group B")].count()
groupC=df.loc[(df['EthnicGroup']=="group C")].count()
groupD=df.loc[(df['EthnicGroup']=="group D")].count()
groupE=df.loc[(df['EthnicGroup']=="group E")].count()


L=[groupA["EthnicGroup"],groupB["EthnicGroup"],groupC["EthnicGroup"],groupD["EthnicGroup"],groupE["EthnicGroup"]]
l=['groupA','groupB','groupC','groupD','groupE']
plt.title("DISTRIBUTION OF ETHNIC GROUP")
plt.pie(L, labels=l, autopct="%1.2f%%")
plt.show()
print(L)
ax = sb.countplot(data=df, x='EthnicGroup')
ax.bar_label(ax.containers[0])

#Bar chart
ax = sb.countplot(data=df, x='EthnicGroup')
ax.bar_label(ax.containers[0])
plt.title("Ethnic Group Distribution")
plt.show()

#MATHS SCORE BY GENDER
plt.figure(figsize=(8, 5))
sb.boxplot(data=df, x="Gender", y="MathScore")
plt.title("Math Scores by Gender")
plt.show()

#READING SCORE BY GENDER
plt.figure(figsize=(8,5))
sb.boxenplot(data=df, x="Gender", y="ReadingScore")
plt.title("READING SCORE BY GENDER")
plt.show()