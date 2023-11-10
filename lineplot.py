import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter, MonthLocator

def lineplot(df, x_column, y_columns, xlabel, ylabel, title, save_path, plot_width=12, plot_height=6):
    """ Function to create a lineplot.

    Arguments:
        df (pd.DataFrame): A dataframe with a column "x" and other columns to be taken as y.
        x_column (str): The header of the x column.
        y_columns (list): A list containing the headers of the columns to plot.
        xlabel (str): Label for the x-axis.
        ylabel (str): Label for the y-axis.
        title (str): Title for the plot.
        save_path (str): Path to save the plot as a PNG file.
        plot_width (int): Width of the plot.
        plot_height (int): Height of the plot.

    This function creates a line plot from the given DataFrame and saves it as a PNG file.
    """
    # Extract 'Date' column and convert it to datetime
    df[x_column] = pd.to_datetime(df[x_column], format='%d-%m-%Y')

    # Reduce the width by 20%
    reduced_width = plot_width * 0.8

    plt.figure(figsize=(reduced_width, plot_height))

    # Plot each specified column
    for y_column in y_columns:
        plt.plot(df[x_column], df[y_column], label=y_column)

    # Labeling
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)

    # Set the x-axis ticks to be every month
    plt.gca().xaxis.set_major_locator(MonthLocator())

    # Format the dates on the x-axis
    date_format = DateFormatter("%Y-%m-%d")
    plt.gca().xaxis.set_major_formatter(date_format)

    plt.xticks(rotation=45)  # Rotate x-axis labels for better visibility
    plt.legend()

    # Save as PNG
    plt.savefig(save_path)
    plt.show()

    return

# Example usage
csv_file_path = 'spotify.csv'
data = pd.read_csv(csv_file_path, delimiter=',')  # Specify the delimiter as ','

# The'Date' is on x-axis and other columns are y-axes
x_column = 'Date'
y_columns = data.columns[1:]  # Exclude the 'Date' column
xlabel = 'Date'
ylabel = 'Number of Times Streamed'
title = 'Number of Times Popular Albums Streamed on Spotify per Day'
save_path = 'lineplot.png'

# Reduce the width by 20%
lineplot(data, x_column, y_columns, xlabel, ylabel, title, save_path, plot_width=12)
