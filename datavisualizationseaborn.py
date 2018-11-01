#https://www.codecademy.com/courses/data-visualization-python/lessons/learn-seaborn-introduction/exercises/intro-seaborn?action=resume_content_item
'''
Seaborn is a Python data visualization library that provides simple code to create elegant visualizations for statistical exploration and insight. Seaborn is based on Matplotlib:
Seaborn provides a more visually appealing plotting style and concise syntax.
Seaborn natively understands Pandas DataFrames, making it easier to plot data directly from CSVs.
Seaborn can easily summarize Pandas DataFrames with many rows of data into aggregated charts.
Pandas is a data analysis library for Python that provides easy-to-use data structures and allows you to organize and manipulate datasets so they can be visualized. To fully leverage the power of Seaborn, it is best to prepare your data using Pandas.
'''

#Learn Seaborn Introduction
#DataFrames contain data structured into rows and columns. DataFrames look similar to other data tables you may be familiar with, but they are designed specifically to be used with Python.
#To create a DataFrame from a local CSV file you would use the syntax df = pd.read_csv('file_name.csv')
import pandas as pd
import seaborn as sns
import numpy as np
from matplotlib import pyplot as plt
df = pd.read_csv('survey.csv') #df is DataFrame
# sns.barplot(x='Age Range', y='Response', hue='Gender', data=df) x and y are the column headers in the variable df .csv file
plt.show()
#print(df.head())  #return the first five rows from the variable df

df = pd.read_csv('results.csv')
# print(df) #return all rows from the variable df
# sns.barplot(x="Gender", y="Mean Satisfaction", data=df) #x and y are the column headers in the variable df .csv file
plt.show()

gradebook = pd.read_csv("gradebook.csv")
# print(gradebook)
# assignment1 = gradebook[gradebook.assignment_name == "Assignment 1"] #assignment_name is a column containing Assignment 1 and Assignment 2
# print(assignment1)
'''
   PRIKEY student assignment_name  grade
0       0     Amy    Assignment 1     75
2       2     Bob    Assignment 1     99
4       4   Chris    Assignment 1     72
6       6     Dan    Assignment 1     88
8       8   Ellie    Assignment 1     91
'''
# assignment1_median = np.median(assignment1.grade)
# print(assignment1_median) #print 88.0
# sns.barplot(x="student", y="grade", data=gradebook) #RM:  default is averaging the grades plotting the bar chart.  Also by default Seaborn place error bars.   Seaborn uses something called a bootstrapped confidence interval. Roughly speaking, this interval means that "based on this data, 95% of similar situations would have an outcome within this range"
# sns.barplot(x="assignment_name", y="grade", data=gradebook) #RM:  default is averaging the two assignments plotting the bar chart.  Also by default Seaborn place error bars.   Seaborn uses something called a bootstrapped confidence interval. Roughly speaking, this interval means that "based on this data, 95% of similar situations would have an outcome within this range"
plt.show()
# sns.barplot(data=gradebook, x="student", y="grade", ci="sd") #use standard deviation for your error bars, you can pass in the keyword argument ci="sd" to sns.barplot() which will represent one standard deviation
plt.show()

df = pd.read_csv('survey.csv') #df is DataFrame
# sns.barplot(x="Gender", y="Response", data=df, estimator=len) #count all responses by gender
plt.show()
# sns.barplot(x="Gender", y="Response", data=df, estimator=np.median) #median response by gender
plt.show()

df = pd.read_csv('survey.csv') #df is DataFrame
# sns.barplot(data=df, x="Gender", y="Response", hue="Age Range") #We can compare both the Gender and Age Range factors at once by using the keyword hue.
plt.show() #display gender x-axis, response y-axis, average responses x-axis gender and by different bars age groups
# sns.barplot(data=df, x="Age Range", y="Response", hue="Gender") #We can compare both the Age Range and Gender factors at once by using the keyword hue.
plt.show() #display age range x-axis, response y-axis, average responses x-axis age range and by different bars gender
'''
To review the seaborn workflow:
1. Ingest data from a CSV file to Pandas DataFrame.  df = pd.read_csv('file_name.csv')
2. Set sns.barplot() with desired values for x, y, and set data equal to your DataFrame.  sns.barplot(data=df, x='X-Values', y='Y-Values')
3. Set desired values for estimator and hue parameters.  sns.barplot(data=df, x='X-Values', y='Y-Values', estimator=len, hue='Value')
4. Render the plot using plt.show().  plt.show()
'''

#Learn Seaborn: Distributions
#Seaborn offers another option for graphing distributions: KDE Plots.
#KDE stands for Kernel Density Estimator. A KDE plot gives us the sense of a univariate as a curve. A univariate dataset only has one variable and is also referred to as being one-dimensional, as opposed to bivariate or two-dimensional datasets which have two variables.
#KDE plots are preferable to histograms because depending on how you group the data into bins and the width of the bins, you can draw wildly different conclusions about the shape of the data. Using a KDE plot can mitigate these issues, because they smooth the datasets, allow us to generalize over the shape of our data, and aren't beholden to specific data points.
#To plot a KDE in Seaborn, we use the method sns.kdeplot().  A KDE plot takes the following arguments:  data - the univariate dataset being visualized, like a Pandas DataFrame, Python list, or NumPy array.  shade - a boolean that determines whether or not the space underneath the curve is shaded.
#The box plot (also known as a box-and-whisker plot) can tell us about how our dataset is distributed, like a KDE plot. But it shows us the range of our dataset, gives us an idea about where a significant portion of our data lies, and whether or not any outliers are present.
#Let's examine how we interpret a box plot:  The box represents the interquartile range.  The line in the middle of the box is the median.  The end lines are the first and third quartiles.  The diamonds show outliers.
#To plot a box plot in Seaborn, we use the method sns.boxplot().  A box plot takes the following arguments:  data - the univariate dataset being visualized, like a Pandas DataFrame, Python list, or NumPy array.  x - a one-dimensional set of values, like a Series, list, or array.  y - a second set of one-dimensional data.
#Violin plots provide more information than box plots because instead of mapping each individual data point, we get an estimation of the dataset.
#There are two KDE plots that are symmetrical along the center line.  A white dot represents the median.  The thick black line in the center of each violin represents the interquartile range.  The lines that extend from the center are the confidence intervals - just as we saw on the bar plots, a violin plot also displays the 95% confidence interval.
#To plot a violin plot in Seaborn, we use the method sns.violinplot().  A violin plot takes the following arguments:  data - the univariate dataset being visualized, like a Pandas DataFrame, Python list, or NumPy array.  x, y, and hue - a one-dimensional set of data, such as a Series, list, or array.  Any of the parameters to the function sns.boxplot().

#Learn Seaborn Quiz
'''
Seaborn improves on Matplotlib by making it easier to plot data directly from CSVs, providing a more visually appealing plotting style, and: easily summarizing Pandas DataFrames with many rows of data into aggregated charts.  Seaborn makes it easy to create and set the most appropriate color palette for a plot, but you still must make the decision about what color palette is the best fit for your particular dataset and plot type.
True or false: When plotting with Seaborn you must aggregate the values in your data yourself before plotting.  False.  One of the most important tasks that Seaborn automates for us is calculating aggregate statistics over large datasets.
There are three keyword arguments that Seaborn's sns.barplot() always needs to create a bar chart. They are:  x, y, data.
Given a dataset that includes information on the number of licks it takes people to get to the center of a tootsie pop, and includes columns with a person's age range, and gender; which is the correct use of hue to create the following chart?  sns.barplot(x="Age Range", y="Number of Licks", hue="Gender", data=df)
Violin Plots are a combination of which of the following plots?  KDE plots and box plots
Standard deviation and bootstrapped confidence intervals are two measurements that can be used for:  Error bars.  To change how error bars are calculated you can use the keyword ci. ci="sd" for example would set the error bars to be calculated using standard deviation.
In Seaborn, bar charts are not able to visualize:  Distributions
Which function would you use to draw the following plot?  sns.kdeplot()  *wave lines like multiple bell shape curves in one chart*
What does the following code snippet do?  df = pd.read_csv("file.csv").  Creates a DataFrame named df made up of the data in the file file.csv.
What does the box in the center of the violin plot represent?  The interquartile range.  A violin plot can also visualize confidence intervals.
'''

#Seaborn Styling, Part 1: Figure Style and Scale
#Seaborn has five built-in themes to style its plots: darkgrid, whitegrid, dark, white, and ticks. Seaborn defaults to using the darkgrid theme for its plots.
#To use any of the preset themes pass the name of it to sns.set_style().
#Spines are the borders of the figure that contain the visualization. By default, an image has four spines.
#You can automatically take away the top and right spines using the sns.despine() function. Note: this function must be called after you have called your plot.  You can also specify how many spines you want to include by calling despine() and passing in the spines you want to get rid of, such as: left, bottom, top, right; e.g. sns.despine(left=True, bottom=True) removes all spines; i.e. set True means remove spine.  
#You can set the visual format, or context, using sns.set_context().  There are three levels of complexity:  Pass in one parameter that adjusts the scale of the plot; Pass in two parameters - one for the scale and the other for the font size; Pass in three parameters - including the previous two, as well as the rc with the style parameter that you want to override.
#There are three levels of complexity:  Pass in one parameter that adjusts the scale of the plot; Pass in two parameters - one for the scale and the other for the font size; Pass in three parameters - including the previous two, as well as the rc with the style parameter that you want to override.  In order of relative size they are: paper, notebook, talk, and poster. The notebook style is the default.
#You are also able to change the size of the text using the font_scale parameter.  You may want to also change the line width so it matches. We do this with the rc parameter.  rc stands for run command.
#more changes using rc= below:
'''
{'axes.labelsize': 17.6,
 'axes.titlesize': 19.200000000000003,
 'font.size': 19.200000000000003,
 'grid.linewidth': 1.6,
 'legend.fontsize': 16.0,
 'lines.linewidth': 2.8000000000000003,
 'lines.markeredgewidth': 0.0,
 'lines.markersize': 11.200000000000001,
 'patch.linewidth': 0.48,
 'xtick.labelsize': 16.0,
 'xtick.major.pad': 11.200000000000001,
 'xtick.major.width': 1.6,
 'xtick.minor.width': 0.8,
 'ytick.labelsize': 16.0,
 'ytick.major.pad': 11.200000000000001,
 'ytick.major.width': 1.6,
 'ytick.minor.width': 0.8}
'''
df = pd.read_csv('survey.csv')
# sns.set_style("white")
# sns.set_context("poster", font_scale = 1.5, rc={"grid.linewidth": 0.6})
# sns.barplot(x="Gender", y="Response", data=df, estimator=len) #count all responses by gender
# sns.despine(left=False, bottom=True)
plt.show()

#Seaborn Styling, Part 2: Color
#You can build color palettes using the function sns.color_palette().  This function can take any of the Seaborn built-in palettes.  # Save a palette to a variable: palette = sns.color_palette("bright") # Use palplot and pass in the variable: sns.palplot(palette) plt.show().
#To select and set a palette in Seaborn, use the command sns.set_palette() and pass in the name of the palette that you would like to use.  If you do not pass in a color palette to sns.color_palette() or sns.set_palette(), Seaborn will use a default set of colors. These defaults improve upon the Matplotlib default color palettes and are one significant reason why people choose to use Seaborn for their data visualizations.  Seaborn has six variations of its default color palette: deep, muted, pastel, bright, dark, and colorblind.
df = pd.read_csv('survey.csv')
# sns.set_palette("pastel")
# sns.barplot(data=df, x="Gender", y="Response", hue="Age Range")
plt.show()
#Seaborn also allows you to style Matplotlib plots. If you're using a plot that only exists in Matplotlib, such as a histogram, you can do so using Seaborn defaults.  To do so, call the sns.set() function before your plot.  RM:  examples are bad.
#Seaborn also allows the use of Color Brewer palettes.  The color palettes are specifically chosen to be easy to interpret when used to represent ordered categories.  Pass the name of any Color Brewer palette directly to any of the color functions.
#RM:  I can't figure out how to use the sns.color_palette to charts.  No examples.
# diverging_colors = sns.color_palette("RdBu", 10)
# sns.palplot(diverging_colors)
# custom_palette = sns.color_palette("Paired", 9)
# sns.palplot(custom_palette)
plt.show()

#Visualizing World Cup Data With Seaborn Freedom Project
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
df = pd.read_csv('WorldCupMatches.csv')
#print(df.head())
'''
   PRIKEY  Year        ...         Home Team Initials Away Team Initials
0       0  1930        ...                        FRA                MEX
1       1  1930        ...                        USA                BEL
2       2  1930        ...                        YUG                BRA
3       3  1930        ...                        ROU                PER
4       4  1930        ...                        ARG                FRA

[5 rows x 21 columns]
'''
df=df[["Year","Home Team Goals","Away Team Goals"]]
df["Total Goals"] = df["Home Team Goals"]+df["Away Team Goals"] #Source:  https://stackoverflow.com/questions/25748683/pandas-sum-dataframe-rows-for-given-columns
print(df.groupby(["Year"])["Home Team Goals"].sum())
print(df.groupby(["Year"])["Total Goals"].sum().reset_index())
print(df.groupby(["Year"])["Home Team Goals","Away Team Goals"].sum())
#also
print(df.groupby(["Year"])[["Home Team Goals"]+["Away Team Goals"]].sum())
print(df.groupby(["Year"])["Total Goals"].sum().reset_index()) #Source:  https://stackoverflow.com/questions/32751229/pandas-sum-by-groupby-but-exclude-certain-columns
datareference = df.groupby(["Year"])["Total Goals"].sum().reset_index() #Source:  https://stackoverflow.com/questions/32751229/pandas-sum-by-groupby-but-exclude-certain-columns
sns.set_style("whitegrid")
sns.set_context("poster", font_scale = 0.25)
plt.figure(figsize=(12,7)) #RM:  .figure() is before .plot()
sns.barplot(x="Year",y="Total Goals", data=datareference)
plt.show()