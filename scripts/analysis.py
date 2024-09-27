import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_sales_distribution(data: pd.DataFrame) -> None:
    """
    Visualize the distribution of sales.

    Parameters:
    - data (pd.DataFrame): The DataFrame containing the sales data.
    """
    plt.figure(figsize=(12, 6))
    sns.histplot(data['Sales'], bins=30, kde=True)
    plt.title('Sales Distribution')
    plt.xlabel('Sales')
    plt.ylabel('Frequency')
    plt.show()

def plot_monthly_sales(data: pd.DataFrame) -> None:
    """
    Display monthly sales trends.

    Parameters:
    - data (pd.DataFrame): The DataFrame containing the sales data.
    """
    data['Month'] = data['Date'].dt.month
    monthly_sales = data.groupby('Month')['Sales'].sum().reset_index()

    plt.figure(figsize=(12, 5))
    sns.lineplot(data=monthly_sales, x='Month', y='Sales', marker='o')
    plt.title('Monthly Sales Trend')
    plt.xlabel('Month')
    plt.ylabel('Total Sales')
    plt.xticks(range(1, 13))
    plt.show()

def plot_promo_sales(data: pd.DataFrame) -> None:
    """
    Analyze average sales with and without promotions.

    Parameters:
    - data (pd.DataFrame): The DataFrame containing the sales data.
    """
    promo_sales = data.groupby('Promo')['Sales'].mean().reset_index()

    plt.figure(figsize=(10, 5))
    sns.barplot(x='Promo', y='Sales', data=promo_sales)
    plt.title('Average Sales with/without Promotions')
    plt.xlabel('Promo')
    plt.ylabel('Average Sales')
    plt.show()

def calculate_summary_statistics(data: pd.DataFrame) -> dict:
    """
    Calculate summary statistics for the sales data.

    Parameters:
    - data (pd.DataFrame): The DataFrame containing the sales data.

    Returns:
    - dict: A dictionary containing the summary statistics.
    """
    summary_stats = {
        'mean': data['Sales'].mean(),
        'std': data['Sales'].std(),
        'min': data['Sales'].min(),
        'max': data['Sales'].max()
    }
    return summary_stats