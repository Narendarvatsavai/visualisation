# Data Source: https://www.kaggle.com/code/alexisbcook/scatter-plots/data?select=insurance.csv
import pandas as pd
import matplotlib.pyplot as plt

def scatterplot(df, x_column, y_column, xlabel, ylabel, title, save_path):
    """ Function to create a scatterplot.

    Arguments:
        df (pd.DataFrame): A dataframe with columns for x and y.
        x_column (str): The header of the x column.
        y_column (str): The header of the y column.
        xlabel (str): Label for the x-axis.
        ylabel (str): Label for the y-axis.
        title (str): Title for the plot.
        save_path (str): Path to save the plot as a PNG file.
        
    Returns:
        None
    """

    plt.figure(figsize=(10, 6))

    # Scatter plot
    plt.scatter(df[x_column], df[y_column], alpha=0.5)

    # Labeling
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)

    # Save as PNG
    plt.savefig(save_path)
    plt.show()

    return None

# Example usage
csv_file_path = 'insurance.csv'
data = pd.read_csv(csv_file_path)

# BMI on x-axis and Insurance premium on y-axis.
x_column = 'bmi'
y_column = 'charges'
xlabel = 'BMI'
ylabel = 'Insurance Premium (Dollers)'
title = 'Scatter Plot of BMI vs. Insurance Premium of US'
save_path = 'scatterplot.png'

scatterplot(data, x_column, y_column, xlabel, ylabel, title, save_path)
