# Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Function to clean data - sets 'Country' as index and drops the 'Country' column
def dataCleaning(data):
    data.set_index(data["Country"], inplace=True)
    data.drop("Country", axis=1, inplace=True)

# Function for plotting the first graph - Adolescent fertility rate
def plottingGraph1(ax, data):
    # Plotting data for various countries
    ax.plot(data.loc["World"], "-.", label="World")
    ax.plot(data.loc["Russia"], "-.", label="Russia")
    ax.plot(data.loc["India"], "-.", label="India")
    ax.plot(data.loc["China"], "-.", label="China")
    ax.plot(data.loc["Brazil"], "-.", label="Brazil")
    # Setting labels, title, and grid
    ax.set_xlabel("Year's (1998-2021)")
    ax.set_ylabel("births per 1,000 women")
    ax.set_title("Adolescent fertility rate (ages 15-19)")
    ax.grid(True, linestyle='--', alpha=0.7)
    ax.legend()

# Function for plotting the second graph - Antiretroviral Therapy Availability
def plottingGraph2(ax, data1, data2):
    ax.plot(data1.loc["India", 2005:], ':', label="female")
    ax.plot(data2.loc["India", 2005:], ':', label="male")
    ax.set_ylabel("Year's (2005-2021)")
    ax.set_xlabel("percentage (%)")
    ax.set_title("India's Antiretroviral Therapy Availability Male vs Female")
    ax.grid(True, linestyle='--', alpha=0.7)
    ax.legend()

# Function for plotting the third graph - Account holders comparison
def plottingGraph3(ax, data1, data2):
    years = data1.columns.astype(int)
    # Horizontal bar plot for account holders
    ax.barh([y - 0.5 for y in years], data1.loc["India"], height=1, color='#89CFF0', alpha=0.5, label="maleAccounts")
    ax.barh([y + 0.5 for y in years], data2.loc["India"], color='#FFD580', alpha=0.5, height=1, label="femaleAccounts")
    ax.set_ylabel("Year's")
    ax.set_xlabel("percentage (%)")
    ax.set_title("Account holders Male vs Female")
    ax.set_yticks(years)
    ax.legend()

# Function for plotting the fourth graph - Parliament members comparison
def plottingGraph4(ax, data1, data2):
    years = data1.columns.astype(int)
    # Bar plot for parliament members and ministries
    ax.bar([x - 0.5 for x in years], data1.loc["India"], width=1, color='#9467bd', alpha=0.5, label="MP's")
    ax.bar([x + 0.5 for x in years], data2.loc["India"], width=1, color='#ffec8b', alpha=0.5, label="Ministeries")
    ax.set_xlabel("Year's")
    ax.set_ylabel("percentage (%)")
    ax.set_title("Member of parliament Member vs Ministers")
    ax.set_xticks(years)
    ax.legend()

# Reading data from excel files
femaleAntiretroviral = pd.read_excel("femaleAntiretroviral.xlsx")
maleAntiretroviral = pd.read_excel("maleAntiretroviral.xlsx")
fertilityRate = pd.read_excel("fertility rate.xlsx")
maleAccounts = pd.read_excel("maleaccount.xlsx")
femaleAccounts = pd.read_excel("femaleaccount.xlsx")
minsters = pd.read_excel("minsters.xlsx")
parliamentMember = pd.read_excel("members.xlsx")

# Cleaning all the datasets
dataCleaning(femaleAntiretroviral)
dataCleaning(maleAntiretroviral)
dataCleaning(fertilityRate)
dataCleaning(maleAccounts)
dataCleaning(femaleAccounts)
dataCleaning(minsters)
dataCleaning(parliamentMember)

# Creating a subplot structure
fig, axes = plt.subplots(2, 2, figsize=(15, 15))
# Plotting each graph
plottingGraph1(axes[0][0], fertilityRate)
plottingGraph2(axes[0][1], femaleAntiretroviral, maleAntiretroviral)
plottingGraph3(axes[1][0], maleAccounts, femaleAccounts)
plottingGraph4(axes[1][1], minsters, parliamentMember)

# Adding a descriptive text/story to the bottom of the figure
story = "\nThis dashboard analyzes gender statistics of India.\n" \
        "1. The Adolescent fertility rate comes down"\
         "drastically in India from 110 out of 1000 to 17,\n" \
        "   reflecting a shift towards female"\
         "education and empowerment.\n" \
        "2. Antiretroviral therapy availability "\
        "increased from 0 to 70% for females and 68% for males,\n" \
        "   showing an increase in healthcare accessibility and development.\n" \
        "3. Account holders started with a male "\
        "lead and by 2021, both genders became equal,\n" \
        "   indicating empowerment.\n" \
        "4. Members of parliament and ministers increased,"\
        " with ministers' numbers overtaking MPs,\n" \
        "   showing increased representation of women."
student_details = "Name: B. Sai Deepak\nID: 22083000"
Title = "India's Gender Statistics"

# Adding text elements to the figure
fig.text(0.01, 0.01, story, ha='left', fontsize=10)
fig.text(0.95, 0.01, student_details, ha='right', fontsize=14)

# Setting the title of the figure
fig.suptitle(Title, fontsize=16, y=0.99, weight='bold')

# Adjust layout and save the figure
plt.tight_layout(rect=[0, 0.15, 1, 1])
plt.savefig('22083000.png', dpi=300)
