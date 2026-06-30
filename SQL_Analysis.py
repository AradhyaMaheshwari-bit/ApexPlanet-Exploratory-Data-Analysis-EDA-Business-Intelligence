# import pandas as pd
# import sqlite3

# # Load cleaned dataset
# df = pd.read_excel("Cleaned_ApexPlanet_DataAnalytics_Dataset.xlsx")

# # Create SQLite database
# conn = sqlite3.connect("Sales_Database.db")

# # Store dataset as SQL table
# df.to_sql("Sales", conn, if_exists="replace", index=False)

# print("Database created successfully!")

# queries = {
#     "Total Revenue": """
#         SELECT SUM(Total_Sales) AS Total_Revenue
#         FROM Sales;
#     """,

#     "Revenue by Category": """
#         SELECT Category,
#                SUM(Total_Sales) AS Revenue
#         FROM Sales
#         GROUP BY Category
#         ORDER BY Revenue DESC;
#     """,

#     "Top Products": """
#         SELECT Product,
#                SUM(Total_Sales) AS Revenue
#         FROM Sales
#         GROUP BY Product
#         ORDER BY Revenue DESC;
#     """,

#     "Revenue by City": """
#         SELECT City,
#                SUM(Total_Sales) AS Revenue
#         FROM Sales
#         GROUP BY City
#         ORDER BY Revenue DESC;
#     """,

#     "Monthly Revenue": """
#         SELECT Month,
#                SUM(Total_Sales) AS Revenue
#         FROM Sales
#         GROUP BY Month
#         ORDER BY Month;
#     """,

#     "Gender-wise Revenue": """
#         SELECT Gender,
#                SUM(Total_Sales) AS Revenue
#         FROM Sales
#         GROUP BY Gender;
#     """,

#     "Top Customers": """
#         SELECT Customer_Name,
#                SUM(Total_Sales) AS Revenue
#         FROM Sales
#         GROUP BY Customer_Name
#         ORDER BY Revenue DESC
#         LIMIT 10;
#     """
# }

# for title, query in queries.items():
#     print("\n" + "=" * 60)
#     print(title)
#     print("=" * 60)

#     result = pd.read_sql_query(query, conn)
#     print(result)

#     # Save each result to CSV
#     filename = title.replace(" ", "_") + ".csv"
#     result.to_csv(filename, index=False)

# conn.close()

# print("\nAll SQL queries executed successfully!")

import pandas as pd
import sqlite3

# Load dataset
df = pd.read_excel("Cleaned_ApexPlanet_DataAnalytics_Dataset.xlsx")

# Create SQLite database
conn = sqlite3.connect("Sales_Database.db")
df.to_sql("Sales", conn, if_exists="replace", index=False)

queries = {
    "Total Revenue": """
        SELECT SUM(Total_Sales) AS Total_Revenue
        FROM Sales;
    """,

    "Revenue by Category": """
        SELECT Category, SUM(Total_Sales) AS Revenue
        FROM Sales
        GROUP BY Category
        ORDER BY Revenue DESC;
    """,

    "Top Products": """
        SELECT Product, SUM(Total_Sales) AS Revenue
        FROM Sales
        GROUP BY Product
        ORDER BY Revenue DESC;
    """,

    "Revenue by City": """
        SELECT City, SUM(Total_Sales) AS Revenue
        FROM Sales
        GROUP BY City
        ORDER BY Revenue DESC;
    """,

    "Monthly Revenue": """
        SELECT Month, SUM(Total_Sales) AS Revenue
        FROM Sales
        GROUP BY Month
        ORDER BY Month;
    """,

    "Gender-wise Revenue": """
        SELECT Gender, SUM(Total_Sales) AS Revenue
        FROM Sales
        GROUP BY Gender;
    """,

    "Top Customers": """
        SELECT Customer_Name, SUM(Total_Sales) AS Revenue
        FROM Sales
        GROUP BY Customer_Name
        ORDER BY Revenue DESC
        LIMIT 10;
    """
}

# Save all results into one Excel workbook
with pd.ExcelWriter("SQL_Results.xlsx", engine="openpyxl") as writer:
    for title, query in queries.items():
        print("\n" + "=" * 60)
        print(title)
        print("=" * 60)

        result = pd.read_sql_query(query, conn)
        print(result)

        # Excel sheet names are limited to 31 characters
        result.to_excel(writer, sheet_name=title[:31], index=False)

conn.close()

print("\nSQL analysis completed successfully!")
print("Results saved to SQL_Results.xlsx")