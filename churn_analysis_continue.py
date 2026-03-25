import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Telecom_customer_Churn.csv")
print(df.head())


df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

df = df.dropna()

df.reset_index(drop=True, inplace=True)
               
print("Cleaning done")
print(df.shape)               

df.to_csv("Cleaned_churn_data.csv", index=False)
               
print("Cleaned dataset saved successfully")


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


plt.figure(figsize=(6,4))
sns.histplot(df['tenure'], bins=30)
plt.title('Customer Tenure Distribution')
plt.savefig("tenure_distribution.png")
plt.show()


plt.figure(figsize=(8,5))
sns.countplot(x='InternetService', hue='Churn', data=df)
plt.title('Churn by Internet Service')
plt.savefig("churn_by_internet.png")
plt.show()



with open("churn_insights.txt", "w") as f:
    f.write("Customer Churn Analysis Insights\n\n")

    f.write("1. Churn Distribution:\n")
    f.write("Most customer did not churn, but a significant portion left the telecom service.\n\n")

    f.write("2. Churn by Contract Type:\n")
    f.write("Customers with month-to-month contracts have the highest churn rate compared to one-year or two-year contracts.\n\n")

    f.write("3. Monthly Charges vs Churn:\n")
    f.write("Customers paying higher monthly charges tend to churn more frequently.\n\n")

    f.write("4. Tenure Distribution:\n")
    f.write("Customers with shorter tenure are more likely to churn.\n\n")
            
    f.write("5. Churn by Internet Service:\n")
    f.write("Certain internet sevice types show higher churn compared to other.\n\n")

print("Insights file created successfully")          

            
       
