# E-Commerce Data Insights (Console Version)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Generate synthetic e-commerce dataset
np.random.seed(42)
products = ['Laptop', 'Smartphone', 'Tablet', 'Headphones', 'Smartwatch']
users = [f'User{i}' for i in range(1, 101)]
dates = pd.date_range(start='2024-01-01', periods=60)
data = []

for _ in range(1000):
    user = np.random.choice(users)
    product = np.random.choice(products)
    quantity = np.random.randint(1, 5)
    review = np.random.randint(1, 6)
    order_time = np.random.choice(dates)
    data.append([user, product, quantity, review, order_time])

df = pd.DataFrame(data, columns=['User', 'Product', 'Quantity', 'Review', 'OrderDate'])
df.to_csv("ecommerce_data.csv", index=False)
print("Saved dataset as ecommerce_data.csv")

# Filtered dataset (all products)
filtered_df = df.copy()

# Top-selling products
top_products = filtered_df.groupby('Product')['Quantity'].sum().sort_values(ascending=False)
plt.figure(figsize=(8, 5))
top_products.plot(kind='bar', color='skyblue')
plt.title("Top-Selling Products")
plt.ylabel("Total Quantity Sold")
plt.tight_layout()
plt.savefig("top_selling_products.png")
plt.show()

# Sales over time
sales_by_day = filtered_df.groupby('OrderDate')['Quantity'].sum()
plt.figure(figsize=(10, 5))
sales_by_day.plot(kind='line', marker='o', color='green')
plt.title("Daily Sales Quantity Over Time")
plt.ylabel("Quantity Sold")
plt.xlabel("Date")
plt.tight_layout()
plt.savefig("sales_over_time.png")
plt.show()

# User retention (users with multiple purchases)
repeat_users = df['User'].value_counts()
retained = (repeat_users > 1).sum()
one_time = (repeat_users == 1).sum()
labels = ['Repeat Users', 'One-Time Users']
sizes = [retained, one_time]
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%', colors=['lightgreen', 'lightcoral'])
ax.axis('equal')
plt.title("User Retention")
plt.tight_layout()
plt.savefig("user_retention_pie.png")
plt.show()

# Display data table
print("\nSample Data:")
print(df.head())
