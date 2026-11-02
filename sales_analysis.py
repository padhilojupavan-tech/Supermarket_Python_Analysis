
import pandas as pd
import matplotlib.pyplot as plt



#  LOAD DATASET


df = pd.read_csv("Supermarket_Sales_Analysis_Dataset.csv")

# Convert Date column
df["Date"] = pd.to_datetime(df["Date"])


# CALCULATE KPIs


total_sales = df["Sales"].sum()
average_sales = df["Sales"].mean()
total_orders = df["Order ID"].count()


#  SALES ANALYSIS


# Sales by Category
category_sales = df.groupby("Category")["Sales"].sum()

# Sales by Product
product_sales = df.groupby("Product")["Sales"].sum()

# Sales by Location
location_sales = df.groupby("Location")["Sales"].sum()

# Monthly Sales (chronological order)
monthly_sales = df.groupby(
    df["Date"].dt.month
)["Sales"].sum()


#  BUSINESS INSIGHTS


top_product = product_sales.idxmax()
top_category = category_sales.idxmax()
top_location = location_sales.idxmax()


#  CREATE DASHBOARD


fig, axes = plt.subplots(2, 2, figsize=(15, 9))

fig.suptitle(
    "SUPERMARKET SALES DASHBOARD",
    fontsize=20,
    fontweight="bold"
)

# KPI CARDS
fig.text(
    0.18, 0.91,
    f"TOTAL SALES\nRs. {total_sales:,.2f}",
    ha="center",
    fontsize=13,
    fontweight="bold"
)

fig.text(
    0.50, 0.91,
    f"AVERAGE SALES\nRs. {average_sales:,.2f}",
    ha="center",
    fontsize=13,
    fontweight="bold"
)

fig.text(
    0.82, 0.91,
    f"TOTAL ORDERS\n{total_orders}",
    ha="center",
    fontsize=13,
    fontweight="bold"
)


#  CHART  SALES BY CATEGORY


category_sales.plot(
    kind="bar",
    ax=axes[0, 0],
    title="Sales by Category"
)

axes[0, 0].set_xlabel("Category")
axes[0, 0].set_ylabel("Total Sales")
axes[0, 0].tick_params(axis="x", rotation=30)

#  MONTHLY SALES TREND


monthly_sales.plot(
    kind="line",
    marker="o",
    linewidth=2,
    ax=axes[0, 1],
    title="Monthly Sales Trend"
)

axes[0, 1].set_xticks([1, 2, 3])
axes[0, 1].set_xticklabels(
    ["January", "February", "March"]
)

axes[0, 1].set_xlabel("Month")
axes[0, 1].set_ylabel("Total Sales")

#  SALES BY LOCATION


location_sales.plot(
    kind="bar",
    ax=axes[1, 0],
    title="Sales by Location"
)

axes[1, 0].set_xlabel("Location")
axes[1, 0].set_ylabel("Total Sales")
axes[1, 0].tick_params(axis="x", rotation=25)


#  SALES BY PRODUCT


product_sales.sort_values().plot(
    kind="barh",
    ax=axes[1, 1],
    title="Sales by Product"
)

axes[1, 1].set_xlabel("Total Sales")
axes[1, 1].set_ylabel("Product")


# BUSINESS INSIGHTS


fig.text(
    0.5, 0.025,
    f"Top Product: {top_product}  |  "
    f"Top Category: {top_category}  |  "
    f"Top Location: {top_location}",
    ha="center",
    fontsize=12,
    fontweight="bold"
)


#  FINAL DASHBOARD SETTINGS
plt.tight_layout(rect=[0, 0.08, 1, 0.78])

plt.savefig("dashboard.png", dpi=300, bbox_inches="tight")
plt.show()