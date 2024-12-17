import matplotlib.pyplot as plt
import seaborn as sns


def plot_data(data):
    """
    Function to plot a stock's close price and moving average over time.

    Parameters
    ----------
    data : pandas.DataFrame
        Dataframe containing the stock's close price and moving average over time.

    Returns
    -------
    None

    """
    plt.figure(figsize=(12, 6))
    plt.plot(data["Date"], data["Close"], label="Close Price", color="blue")
    plt.plot(data["Date"], data["Moving Average"], label="Moving Average", color="red")
    plt.xlabel("Data")
    plt.ylabel("Price")
    plt.title("Stock price, moving average")
    plt.legend()
    plt.grid()
    plt.show()

def plot_univariate(data, column, title=None):
    """
    Function to plot a univariate analysis (histogram) of a given column in the data.

    Parameters
    ----------
    data : pandas.DataFrame
        Dataframe containing the data to plot.
    column : str
        Name of the column to plot.
    title : str, optional
        Title to display on the plot. Defaults to "Univariate Analysis of {column}".

    Returns
    -------
    None
    """
    
    plt.figure(figsize=(8, 6))
    sns.histplot(data[column], kde=True, bins=30)
    plt.title(title or f"Univariate Analysis of {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.show()

def plot_bivariate(data, x_column, y_column, title=None):
    """Creates a scatter plot to visualize the relationship between two variables.

    Generates a bivariate scatter plot to explore potential correlations or patterns between two selected columns in a dataset.

    Args:
        data (pandas.DataFrame): Input DataFrame containing the data to be plotted.
        x_column (str): Name of the column to be used for the x-axis.
        y_column (str): Name of the column to be used for the y-axis.
        title (str, optional): Custom title for the plot. Defaults to an auto-generated title.

    Examples:
        >>> plot_bivariate(stock_data, 'Volume', 'Close')
    """

    plt.figure(figsize=(8, 6))
    sns.scatterplot(x=data[x_column], y=data[y_column])
    plt.title(title or f"Bivariate Analysis: {x_column} vs {y_column}")
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.show()



# Visualize headline lengths
def plot_headline_length(data):
    sns.histplot(data['headline_length'], bins=30, kde=True, color='skyblue')
    plt.title("Distribution of Headline Lengths")
    plt.xlabel("Headline Length")
    plt.ylabel("Frequency")
    plt.show()

def plot_top_publishers(publisher_counts):
    top_publishers = publisher_counts.head(10)  # Show top 10 publishers
    top_publishers.plot(kind='bar', color='lightcoral', figsize=(10, 6))
    plt.title("Top 10 Publishers by Article Count")
    plt.xlabel("Publisher")
    plt.ylabel("Number of Articles")
    plt.show()




# Visualize the top keywords
def plot_top_keywords(word_frequencies):
    word_frequencies.head(10).plot(kind='barh', color='orange', figsize=(8, 6))
    plt.title("Top 10 Keywords in Headlines")
    plt.xlabel("Frequency")
    plt.show()

# Plot publication frequency over time
def plot_publication_frequency(daily_publications):
    plt.figure(figsize=(12, 6))
    daily_publications.plot(kind='line', color='blue', marker='o')
    plt.title("Daily Publication Frequency")
    plt.xlabel("Date")
    plt.ylabel("Number of Articles")
    plt.grid(True)
    plt.show()

# Plot the distribution of publishing times
def plot_publishing_times(hourly_publications):
    plt.figure(figsize=(12, 6))
    hourly_publications.plot(kind='bar', color='orange')
    plt.title("Articles Published by Hour of Day")
    plt.xlabel("Hour of Day (24-hour format)")
    plt.ylabel("Number of Articles")
    plt.grid(axis='y')
    plt.show()