import pandas as pd

# Load Cleaned Dataset
df = pd.read_excel("Cleaned_ApexPlanet_DataAnalytics_Dataset.xlsx")

print("="*60)
print("EXPLORATORY DATA ANALYSIS")
print("="*60)

# Dataset Information
print("\nDataset Shape")
print(df.shape)

print("\nColumn Names")
print(df.columns.tolist())

print("\nData Types")
print(df.dtypes)

# Summary Statistics
print("\nSummary Statistics")
print(df.describe())

# Missing Values
print("\nMissing Values")
print(df.isnull().sum())

# Category Counts
print("\nCategory Distribution")
print(df["Category"].value_counts())

# City Counts
print("\nCity Distribution")
print(df["City"].value_counts())

# Gender Counts
print("\nGender Distribution")
print(df["Gender"].value_counts())

# Product Counts
print("\nProduct Distribution")
print(df["Product"].value_counts())

# Revenue by Category
print("\nRevenue by Category")
print(df.groupby("Category")["Total_Sales"].sum().sort_values(ascending=False))

# Revenue by City
print("\nRevenue by City")
print(df.groupby("City")["Total_Sales"].sum().sort_values(ascending=False))

# Monthly Revenue
print("\nMonthly Revenue")
print(df.groupby("Month")["Total_Sales"].sum())

# Top Products
print("\nTop Products")
print(df.groupby("Product")["Total_Sales"].sum().sort_values(ascending=False))

# Top Customers
print("\nTop Customers")
print(df.groupby("Customer_Name")["Total_Sales"].sum().sort_values(ascending=False).head(10))

# Correlation
print("\nCorrelation Matrix")
print(df[["Age","Quantity","Unit_Price","Total_Sales"]].corr())

print("\nEDA Completed Successfully!")

import matplotlib.pyplot as plt

# Revenue by Category
plt.figure(figsize=(8,5))
df.groupby("Category")["Total_Sales"].sum().sort_values().plot(kind="bar")
plt.title("Revenue by Category")
plt.xlabel("Category")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("Revenue_by_Category.png")
plt.show()

# Revenue by City
plt.figure(figsize=(8,5))
df.groupby("City")["Total_Sales"].sum().sort_values().plot(kind="bar")
plt.title("Revenue by City")
plt.xlabel("City")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("Revenue_by_City.png")
plt.show()

# Monthly Revenue
plt.figure(figsize=(10,5))
df.groupby("Month")["Total_Sales"].sum().plot(marker="o")
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.grid(True)
plt.tight_layout()
plt.savefig("Monthly_Revenue.png")
plt.show()

# Product Distribution
plt.figure(figsize=(8,5))
df["Product"].value_counts().plot(kind="bar")
plt.title("Product Distribution")
plt.xlabel("Product")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("Product_Distribution.png")
plt.show()

# Age Distribution
plt.figure(figsize=(8,5))
plt.hist(df["Age"], bins=10)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("Age_Distribution.png")
plt.show()

print("\nCharts saved successfully!")