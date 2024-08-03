import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Parameters
np.random.seed(42)
num_rows = 50
categories = ["Electronics", "Clothing", "Home & Kitchen", "Books", "Toys"]

# Generate data
product_names = [f"Product {i+1}" for i in range(num_rows)]
product_categories = np.random.choice(categories, num_rows)

# Generate random dates
start_date = datetime(2023, 1, 1)
dates = [start_date + timedelta(days=np.random.randint(0, 90)) for _ in range(num_rows)]

# Generate random quantities, sales total, and profit total
quantities = np.random.randint(1, 20, num_rows)
sales_totals = quantities * np.random.uniform(10, 100, num_rows)
profits_totals = sales_totals * np.random.uniform(0.1, 0.5, num_rows)

# Generate random weather conditions
weather_conditions = np.random.choice(["Sunny", "Rainy", "Cloudy", "Snowy"], num_rows)

# Create DataFrame
sample_data = pd.DataFrame(
    {
        "category": product_categories,
        "product_name": product_names,
        "dates": dates,
        "quantities": quantities,
        "sales_totals": sales_totals,
        "profits_totals": profits_totals,
        "weather_conditions": weather_conditions,
    }
)

# Save to CSV
sample_data.to_csv("../sample_sales_data.csv", index=False, encoding="utf-8")

sample_data.head()
