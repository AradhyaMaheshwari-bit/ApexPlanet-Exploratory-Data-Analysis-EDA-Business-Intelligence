# Exploratory Data Analysis (EDA) Report

## ApexPlanet Internship – Task 2

### Submitted By

**Name:** Aradhya Maheshwari

**Internship Domain:** Data Analytics

---

# 1. Introduction

The objective of this Exploratory Data Analysis (EDA) is to understand the sales dataset by identifying trends, patterns, relationships, and business insights. The analysis helps prepare the dataset for future business intelligence and dashboard development.

---

# 2. Dataset Overview

| Attribute | Value |
|------------|--------|
| Number of Records | 1000 |
| Number of Columns | 16 |
| Missing Values | None |
| Duplicate Records | None |
| Dataset Status | Clean and Ready for Analysis |

Columns Included:

- Order_ID
- Order_Date
- Customer_ID
- Customer_Name
- Age
- Gender
- City
- Product
- Category
- Quantity
- Unit_Price
- Total_Sales
- Year
- Month
- Quarter
- Day_Name

---

# 3. Descriptive Statistics

### Age

- Minimum: 18
- Maximum: 65
- Average: 41.35 Years

### Quantity

- Minimum: 1
- Maximum: 10
- Average: 5.44

### Unit Price

- Average: ₹25,486.78

### Total Sales

- Average Revenue per Transaction:

₹139,399.44

Maximum Revenue:

₹493,677.50

---

# 4. Missing Value Analysis

No missing values were found in the cleaned dataset.

The preprocessing performed in Task 1 ensured that:

- Missing Age values were replaced using the Median.
- Missing City values were replaced using the Mode.

---

# 5. Category Analysis

Electronics generated the highest revenue.

Revenue Ranking

1. Electronics
2. Education
3. Grocery
4. Furniture
5. Fashion

(Insert Revenue_by_Category.png)

---

# 6. City Analysis

Top Revenue Generating Cities

1. Patna
2. Kolkata
3. Bengaluru
4. Mumbai
5. Hyderabad

(Insert Revenue_by_City.png)

---

# 7. Monthly Sales Trend

Sales remained relatively consistent throughout the year.

Highest revenue months:

- March
- June
- November

(Insert Monthly_Revenue.png)

---

# 8. Product Analysis

Products ranked by revenue:

1. Laptop
2. Mobile
3. Book
4. Rice
5. Chair
6. Shoes

(Insert Product_Distribution.png)

---

# 9. Customer Demographics

Gender Distribution

Male : 511

Female : 489

Average Customer Age

41 Years

(Insert Age_Distribution.png)

---

# 10. Correlation Analysis

| Variables | Correlation |
|------------|------------|
| Quantity vs Sales | 0.646 |
| Unit Price vs Sales | 0.686 |
| Age vs Sales | 0.001 |

Observations

- Unit Price has the strongest relationship with Total Sales.
- Quantity also has a strong positive relationship with Sales.
- Customer Age has almost no impact on Total Sales.

---

# 11. Key Business Insights

• Electronics contributes the highest revenue.

• Laptops are the highest revenue-generating product.

• Patna is the highest revenue-generating city.

• Male and Female customers contribute almost equally.

• Average customer age is approximately 41 years.

• Sales are evenly distributed throughout the year with peaks in March, June, and November.

• Revenue depends more on Unit Price and Quantity than customer age.

---

# 12. Conclusion

The dataset is clean, complete, and suitable for advanced business intelligence tasks.

The analysis identified major revenue contributors, customer trends, city-wise performance, and sales behavior.

These insights will be used in the next stages to answer business questions using SQL and design business dashboards.