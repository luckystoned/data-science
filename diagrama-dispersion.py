import pandas as pd
import seaborn as sns

iris = pd.read_csv('Data Science/iris.csv')
iris.head()

#scatter plot
sns.scatterplot(data=iris, x="SepalLengthCm", y="PetalLengthCm", hue="Species")

#join plot
sns.jointplot(data=iris, x="SepalLengthCm", y="PetalLengthCm", hue="Species")

#box plot
sns.boxplot(data=iris, x="Species", y="SepalLengthCm")

#Bar plot
sns.barplot(data=iris, x="Species", y="SepalLengthCm")