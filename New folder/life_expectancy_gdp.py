
# coding: utf-8

# # Introduction
# 
# For this project, you will act as a data researcher for the World Health Organization. You will investigate if there is a strong correlation between the economic output of a country and the life expectancy of its citizens.  
# 
# During this project, you will analyze, prepare, and plot data, and seek to answer questions in a meaningful way.
# 
# After you perform analysis, you'll be creating an article with your visualizations to be featured in the fictional "Time Magazine".
# 
# **Focusing Questions**: 
# + Has life expectancy increased over time in the six nations?
# + Has GDP increased over time in the six nations?
# + Is there a correlation between GDP and life expectancy of a country?
# + What is the average life expactancy in these nations?
# + What is the distribution of that life expectancy?
# 
# GDP Source:[World Bank](https://data.worldbank.org/indicator/NY.GDP.MKTP.CD)national accounts data, and OECD National Accounts data files.
# 
# Life expectancy Data Source: [World Health Organization](http://apps.who.int/gho/data/node.main.688)
# 

# ## Step 1. Import Python Modules

# Import the modules that you'll be using in this project:
# - `from matplotlib import pyplot as plt`
# - `import pandas as pd`
# - `import seaborn as sns`

# In[1]:

from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np


# ## Step 2 Prep The Data

# To look for connections between GDP and life expectancy you will need to load the datasets into DataFrames so that they can be visualized.
# 
# Load **all_data.csv** into a DataFrame called `df`. Then, quickly inspect the DataFrame using `.head()`.
# 
# Hint: Use `pd.read_csv()`
# 

# In[2]:

df = pd.read_csv("\\\\wanlink.us\\DFSROOT\\BU\\GI\\Intermediary\\Asset Management\\Users\\bmoran\\Jupyter\\all_data.csv")
df.head()


# ## Step 3 Examine The Data

# The datasets are large and it may be easier to view the entire dataset locally on your computer. You can open the CSV files directly from the folder you downloaded for this project.
# 
# Let's learn more about our data:
# - GDP stands for **G**ross **D**omestic **P**roduct. GDP is a monetary measure of the market value of all final goods and services produced in a time period. 
# - The GDP values are in current US dollars.

# What six countries are represented in the data?

# In[3]:

countries = df.Country.unique()
print countries


# What years are represented in the data?

# In[4]:

years = df.Year.unique()
print years


# ## Step 4 Tweak The DataFrame
# 
# Look at the column names of the DataFrame `df` using `.head()`. 

# In[5]:

df.head()


# What do you notice? The first two column names are one word each, and the third is five words long! `Life expectancy at birth (years)` is descriptive, which will be good for labeling the axis, but a little difficult to wrangle for coding the plot itself. 
# 
# **Revise The DataFrame Part A:** 
# 
# Use Pandas to change the name of the last column to `LEABY`.
# 
# Hint: Use `.rename()`. [You can read the documentation here.](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.rename.html)). </font>

# In[6]:

df.rename(columns={"Life expectancy at birth (years)": "LEABY"}, inplace=True)


# Run `df.head()` again to check your new column name worked.

# In[7]:

df.head()


# ---

# ## Step 5 Bar Charts To Compare Average

# To take a first high level look at both datasets, create a bar chart for each DataFrame:
# 
# A) Create a bar chart from the data in `df` using `Country` on the x-axis and `GDP` on the y-axis. 
# Remember to `plt.show()` your chart!

# In[8]:

df.plot.bar(x='Country',y='GDP')
plt.show()
sns.barplot(data=df,x='Country',y='GDP',estimator=np.mean)
plt.show()


# B) Create a bar chart using the data in `df` with `Country` on the x-axis and `LEABY` on the y-axis.
# Remember to `plt.show()` your chart!

# In[9]:

df.plot.bar(x='Country',y='LEABY')
plt.show()
sns.barplot(data=df,x='Country',y='LEABY',estimator=np.mean)
plt.show()


# What do you notice about the two bar charts? Do they look similar?

# In[ ]:




# ## Step 6. Violin Plots To Compare Life Expectancy Distributions 

# Another way to compare two datasets is to visualize the distributions of each and to look for patterns in the shapes.
# 
# We have added the code to instantiate a figure with the correct dimmensions to observe detail. 
# 1. Create an `sns.violinplot()` for the dataframe `df` and map `Country` and `LEABY` as its respective `x` and `y` axes. 
# 2. Be sure to show your plot

# In[10]:

fig = plt.subplots(figsize=(15, 10)) 
sns.violinplot(data=df,x='Country',y='LEABY')

plt.show()


# What do you notice about this distribution? Which country's life expactancy has changed the most?

#  

# ## Step 7. Bar Plots Of GDP and Life Expectancy over time
# 
# We want to compare the GDPs of the countries over time, in order to get a sense of the relationship between GDP and life expectancy. 
# 
# First, can plot the progession of GDP's over the years by country in a barplot using Seaborn.
# We have set up a figure with the correct dimensions for your plot. Under that declaration:
# 1. Save `sns.barplot()` to a variable named `ax`
# 2. Chart `Country` on the x axis, and `GDP` on the `Y` axis on the barplot. Hint: `ax = sns.barplot(x="Country", y="GDP")`
# 3. Use the `Year` as a `hue` to differentiate the 15 years in our data. Hint: `ax = sns.barplot(x="Country", y="GDP", hue="Year", data=df)`
# 4. Since the names of the countries are long, let's rotate their label by 90 degrees so that they are legible. Use `plt.xticks("rotation=90")`
# 5. Since our GDP is in trillions of US dollars, make sure your Y label reflects that by changing it to `"GDP in Trillions of U.S. Dollars"`. Hint: `plt.ylabel("GDP in Trillions of U.S. Dollars")`
# 6. Be sure to show your plot.
# 

# In[11]:

f, ax = plt.subplots(figsize=(10, 15)) 
ax = sns.barplot()
ax = sns.barplot(x="Country", y="GDP", hue="Year",data=df)
plt.xticks(rotation=90)
plt.ylabel("GDP in Trillions of U.S. Dollars")
plt.show()


# Now that we have plotted a barplot that clusters GDP over time by Country, let's do the same for Life Expectancy.
# 
# The code will essentially be the same as above! The beauty of Seaborn relies in its flexibility and extensibility. Paste the code from above in the cell bellow, and: 
# 1. Change your `y` value to `LEABY` in order to plot life expectancy instead of GDP. Hint: `ax = sns.barplot(x="Country", y="LEABY", hue="Year", data=df)`
# 2. Tweak the name of your `ylabel` to reflect this change, by making the label `"Life expectancy at birth in years"` Hint: `ax.set(ylabel="Life expectancy at birth in years")`
# 

# In[12]:

f, ax = plt.subplots(figsize=(10, 15)) 
ax1 = sns.barplot()
ax1 = sns.barplot(x="Country", y="LEABY", hue="Year",data=df)
plt.xticks(rotation=90)
plt.ylabel("Life expectancy at birth in years")
plt.show()


# What are your first impressions looking at the visualized data?
# 
# - Which countries' bars changes the most?
# - What years are there the biggest changes in the data?
# - Which country has had the least change in GDP over time? 
# - How do countries compare to one another?
# - Now that you can see the both bar charts, what do you think about the relationship between GDP and life expectancy?
# - Can you think of any reasons that the data looks like this for particular countries?

# - The bar chart clearly shows the biggest change in Life expectancy at birth in years is Zimbabwe
# - The 10 year span from 2005 to 2015, Zimbabwe's LEABY jumps from around 45 to 60, a 33% increase. 
# - Zimbabwe had the lowest GDP over the time analyzed.  
# - The gap between countries is vast, even between developed nations, such as the US and Germany, the GDP difference is over 10 fold.
# - It would appear there is a correlation, but there would need to be more analysis done, as Germany's GDP is far from the US's, but they lead the 6 countries studied in LEABY. LEABY is, relatively speaking, fairly match between all countries, except Zimbabwe, whcih also happens to have the lowest GDP. But there we have not tested for correlation, and correlation does not imply causation. 
# - It's clear the gap between 1st and 2nd world counties is shrinking in terms of life expectancy, but the difference between 2nd and 3rd world countries still is vast. 

# Note: You've mapped two bar plots showcasing a variable over time by country, however, bar charts are not traditionally used for this purpose. In fact, a great way to visualize a variable over time is by using a line plot. While the bar charts tell us some information, the data would be better illustrated on a line plot.  We will complete this in steps 9 and 10, for now let's switch gears and create another type of chart.

# ## Step 8. Scatter Plots of GDP and Life Expectancy Data

# To create a visualization that will make it easier to see the possible correlation between GDP and life expectancy, you can plot each set of data on its own subplot, on a shared figure.
# 
# To create multiple plots for comparison, Seaborn has a special (function)[https://seaborn.pydata.org/generated/seaborn.FacetGrid.html] called `FacetGrid`. A FacetGrid takes in a function and creates an individual graph for which you specify the arguments!
#     
# Since this may be the first time you've learned about FacetGrid, we have prepped a fill in the blank code snippet below. 
# Here are the instructors to fill in the blanks from the commented word bank:
# 
# 1. In this graph, we want GDP on the X axis and Life Expectancy on the Y axis.
# 2. We want the columns to be split up for every Year in the data
# 3. We want the data points to be differentiated (hue) by Country.
# 4. We want to use a Matplotlib scatter plot to visualize the different graphs
# 
# 
# Be sure to show your plot!
# 

# In[13]:

# WORDBANK:
# "Year"
# "Country" 
# "GDP" 
# "LEABY" 
# plt.scatter


# Uncomment the code below and fill in the blanks
g = sns.FacetGrid(df, col="Year", hue="Country", col_wrap=4, size=2)
g = (g.map(plt.scatter, 'GDP', 'LEABY', edgecolor="w").add_legend())
plt.show()


# + Which country moves the most along the X axis over the years?
# + Which country moves the most along the Y axis over the years?
# + Is this surprising?
# + Do you think these scatter plots are easy to read? Maybe there's a way to plot that! 

# + China moves the most over the X axis over the years. I.e. has the fastest growth rate of GDP relative to the other countires. 
# + Zimbabwe moves the most over the Y axis over the years.
# + It is surprising on 2 fronts. 1st is the fact that Zimbabwe's LEABY is so low in the 21st century. 2nd is the impressive way they've been able to increase their LEABY over a 15 year window. 
# + The scatter plots do a nice job of scaling the data to make it represantative of all countries in the sample, but the fact that there is a chart for every year makes it a little less useful

# ## Step 9. Line Plots for Life Expectancy

# In the scatter plot grid above, it was hard to isolate the change for GDP and Life expectancy over time. 
# It would be better illustrated with a line graph for each GDP and Life Expectancy by country. 
# 
# FacetGrid also allows you to do that! Instead of passing in `plt.scatter` as your Matplotlib function, you would have to pass in `plt.plot` to see a line graph. A few other things have to change as well. So we have created a different codesnippets with fill in the blanks.  that makes use of a line chart, and we will make two seperate FacetGrids for both GDP and Life Expectancy separately.
# 
# Here are the instructors to fill in the blanks from the commented word bank:
# 
# 1. In this graph, we want Years on the X axis and Life Expectancy on the Y axis.
# 2. We want the columns to be split up by Country
# 3. We want to use a Matplotlib line plot to visualize the different graphs
# 
# 
# Be sure to show your plot!
# 
# 

# In[14]:

# WORDBANK:
# plt.plot
# "LEABY"
# "Year"
# "Country"


# Uncomment the code below and fill in the blanks
g3 = sns.FacetGrid(df, col="Country", col_wrap=3, size=4)
g3 = (g3.map(plt.plot, "Year", "LEABY").add_legend())
plt.show()


# What are your first impressions looking at the visualized data?
# 
# - Which countries' line changes the most?
# - What years are there the biggest changes in the data?
# - Which country has had the least change in life expectancy over time? 
# - Can you think of any reasons that the data looks like this for particular countries?

# - Based on the line graph, it is hard to tell which other countries changes the most after Zimbabwe, but it appears to be China
# - From 2004 to 2015, Zimbabwe's LEABY appears to grow the most
# - It appears Mexico has had the least amount of change over the 15 year window, going from 75 to about 76
# - Mexico currently has the 15h largest economy in terms of GDP in the world, but it is estimated that 42% of Mexico's total population living below the national poverty line, which in turn likely leads to lower life expactancy, despite the relatively large GDP.

# ## Step 10. Line Plots for GDP

# Let's recreate the same FacetGrid for GDP now. Instead of Life Expectancy on the Y axis, we now we want GDP.
# 
# Once you complete and successfully run the code above, copy and paste it into the cell below. Change the variable for the X axis. Change the color on your own! Be sure to show your plot.
# 

# In[15]:


g3 = sns.FacetGrid(df, col="Country", col_wrap=3, size=4)
g3 = (g3.map(plt.plot, "Year", "GDP", color="r").add_legend())
plt.show()


# Which countries have the highest and lowest GDP?

# Looking at the scaled data from the FacetGrid plots, it's easy to ideinitfy with the line chart, GDP plotted on the Y-axis and years on X-axisa, that US consistantly has had the highest GDP over the 15 year period. With Zimbabwe (not quite as clearly) having the lowest. The Seaborn bar plot gives a very easy to read and non-ambigious representtation of US having the highest, and Zimbabwe having the lowest. 

# Which countries have the highest and lowest life expectancy?

# Germany leads the 6 countries in highest life expectatancy over the 15 year window, with Zimbabwe again coming in last. This is clearly seen in both the Seaborn FacetGrid line graph, as well as the Seaborn bar chart.

# ## Step 11 Researching Data Context 

# Based on the visualization, choose one part the data to research a little further so you can add some real world context to the visualization. You can choose anything you like, or use the example question below.
# 
# What happened in China between in the past 10 years that increased the GDP so drastically?

# There are a lot of reasons why China has seen such drastic growth in GDP over the 15 year window studied in this study. First and foremost, Chinas labor laws are far less strict than much of the developed world, allowing them to produce good and services at a much cheaper cost than many other developed nations, giving them a major economic competitive advanctage. China is the world's largest exporter in terms of nomimal goods, and does so in some questionable ways. One example is China's centeral bank (simlilar to the Fed in the US)keeps the USD/CNY to a level such that it is more making it economically sensible (cheaper) for countries and companies to outsource a lot of their production of goods to China vs doing the production domestically. 
# 
# China has also taken advantage of the technogolgy boom over the past 20 years. China has some of the largest technology firms in the world (Alibaba), as well as 2 of the largest energy / oil firms in the world. 
# 
# Also, and possibly the biggest factor in this is China joining the WTO in 2001, giving it access to many trading partners it did not have in the past, allowing it to becaome the economic powerhouse we see today. 

# ## Step 12 Create Blog Post

# Use the content you have created in this Jupyter notebook to create a blog post reflecting on this data.
# Include the following visuals in your blogpost:
# 
# 1. The violin plot of the life expectancy distribution by country
# 2. The facet grid of scatter graphs mapping GDP as a function Life Expectancy by country
# 3. The facet grid of line graphs mapping GDP by country
# 4. The facet grid of line graphs mapping Life Expectancy by country
# 
# 
# We encourage you to spend some time customizing the color and style of your plots! Remember to use `plt.savefig("filename.png")` to save your figures as a `.png` file.
# 
# When authoring your blog post, here are a few guiding questions to guide your research and writing:
# + How do you think the histories and the cultural values of each country relate to its GDP and life expectancy?
# + What would have helped make the project data more reliable? What were the limitations of the dataset?
# + Which graphs better illustrate different relationships??

# In[24]:

# 1 - voilin plot of life expectancy distribution by country 
fig = plt.subplots(figsize=(15, 10)) 
sns.violinplot(data=df,x='Country',y='LEABY')
plt.savefig("\\\\wanlink.us\\DFSROOT\\BU\\GI\\Intermediary\\Asset Management\\Users\\bmoran\\LEABY.png") 
plt.show()



#2 - GDP as function of life expectancy by country
g = sns.FacetGrid(df, col="Year", hue="Country", col_wrap=4, size=2)
g = (g.map(plt.scatter, 'GDP', 'LEABY', edgecolor="w").add_legend())
g.savefig("\\\\wanlink.us\\DFSROOT\\BU\\GI\\Intermediary\\Asset Management\\Users\\bmoran\\LEABY_GDP.png") 
plt.show()



#3 - Line graph of GDP by country
g3 = sns.FacetGrid(df, col="Country", col_wrap=3, size=4)
g3 = (g3.map(plt.plot, "Year", "GDP").add_legend())
g3.savefig("\\\\wanlink.us\\DFSROOT\\BU\\GI\\Intermediary\\Asset Management\\Users\\bmoran\\GDP.png") 
plt.show()

#4 - 
g4 = sns.FacetGrid(df, col="Country", col_wrap=3, size=4)
g4 = (g4.map(plt.plot, "Year", "LEABY",color="r").add_legend())
g4.savefig("\\\\wanlink.us\\DFSROOT\\BU\\GI\\Intermediary\\Asset Management\\Users\\bmoran\\LEABY_LG.png") 
plt.show()

