import pandas as pd
import matplotlib.pyplot as plt

def barplot(df, x_column, y_column, xlabel, ylabel, title, save_path):
    """ Function to create a bar plot.

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

    # Bar plot
    plt.bar(df[x_column], df[y_column])

    # Labeling
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)

    # Save as PNG
    plt.savefig(save_path)
    plt.show()

    return None

# Example usage
excel_file_path = 'Land use per gram of protein.xlsx'
data = pd.read_excel(excel_file_path)

# Assuming 'Food Type' is your x-axis and 'Land Use (in sqm)' is your y-axis
x_column = 'Food Type'
y_column = 'Land Use (in sqm)'
xlabel = 'Food Type'
ylabel = 'Land Use per gram of protein (sqm)'
title = 'Bar Plot of Land Use per gram of protein by Food Type'
save_path = 'barplot.png'

barplot(data, x_column, y_column, xlabel, ylabel, title, save_path)