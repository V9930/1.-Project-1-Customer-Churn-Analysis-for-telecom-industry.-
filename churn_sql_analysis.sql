CREATE TABLE churn_data(
customerID TEXT,
gender TEXT,
SeniorCitizen INT,
Partner TEXT,
Dependents TEXT,
tenure INT,
PhoneService TEXT,
MultipleLines TEXT,
InternetService TEXT,
OnlineSecurity TEXT,
OnlineBackup TEXT,
DeviceProtection TEXT,
TechSupport TEXT,
StreamingTV TEXT,
StreamingMovies TEXT,
Contract TEXT,
PaperlessBilling TEXT,
PaymentMEthod TEXT,
MonthlyCharges NUMERIC,
TotalCharges NUMERIC,
Chrun TEXT
);

ALTER TABLE churn_data
RENAME COLUMN "chrun" TO "churn";

SELECT *
FROM churn_data
LIMIT 10;

Total Customers
SELECT COUNT(*) AS total_customers
FROM churn_data;


SELECT COUNT(*) AS churned_customers
FROM churn_data
WHERE churn = 'Yes';


SELECT
COUNT(CASE WHEN churn='Yes' THEN 1 END)*100.0/
COUNT(*) AS churn_rate
FROM churn_data;


SELECT contract, COUNT(*) AS  churn_count
FROM churn_data
WHERE churn='Yes'
GROUP BY contract
order by churn_count DESC;


SELECT internetservice, COUNT(*) AS churn_count
FROM churn_data
WHERE churn='Yes'
GROUP BY internetservice
ORDER BY churn_count DESC;

SELECT AVG(monthlycharges) AS avg_monthly_charges
FROM churn_data;

SELECT AVG(monthlycharges) AS avg_churn_monthly_charges
FROM churn_data
WHERE churn='Yes';


SELECT paymentmethod, COUNT(*) AS churn_count
FROM churn_data
WHERE churn='Yes'
GROUP BY paymentmethod
ORDER BY churn_count DESC;

SELECT seniorcitizen, COUNT(*) AS churn_count
FROM churn_data
WHERE churn='Yes'
GROUP BY seniorcitizen;

SELECT customerid, monthlycharges
FROM churn_data
ORDER BY monthlycharges DESC
LIMIT 10;

