import pandas as pd

df = pd.read_csv("Telecom_Customer_Churn.csv")

with open("analysis_output.txt", "w") as f:
    f.write("first 5 Rows:\n")
    f.write(str(df.head()))

    f.write("\n\nDataset Shape:\n")
    f.write(str(df.shape))

    f.write("\n\nColumn Name:\n")
    f.write(str(df.columns))

    f.write("\n\nMissing Values:\n")
    f.write(str(df.isnull().sum()))

print("Output saved successfully")    


import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

plt.figure(figsize=(6,4))
sns.countplot(x='Churn', data=df)
plt.title('Customer Churn Distribution')
plt.savefig("churn_distribution.png")
plt.show()


plt.figure(figsize=(6,4))
sns.hislot(df['tenure'], bins=30, kde=False)
plt.title('Customer Tenure Distribution')
plt.savefig("tenure_distribution.png")
plt.show()

plt.figure(figsize=(8,5))
sns.countplot(x='Contract', hue='Churn', data=df)
plt.title('Churn by Contract Type')
plt.savefig("churn_by_contract.png")
plt.show()

plt.figure(figsize=(6,4))
sns.boxplot(x='Churn', y='MonthlyCharges', data=df)
plt.title('Monthly Charges vs Churn')
plt.savefig("monthly_charges_vs_churn.png")
plt.show()

plt.figure(figsize=(8,5))
sns.countplot(x='InternetService', hue='Churn',data=df)
plt.title('Churn by Internet Service')
plt.savefig("churn_by_internet.png")
plt.show()



