# -*- coding: utf-8 -*-
"""
Created on Tue Mar 11 15:44:44 2025

@author: pturrent
"""

#################################################################

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Load the data
df1 = pd.read_csv(r'C:\Users\pturrent\Documents\Iordonova Lab\SPC Ephys\Clean data for python\Supression data combined_CSV.csv')

#df1 = pd.read_csv(r'C:\Users\pturrent\Documents\Iordonova Lab\SPC pilot\Suppresion data for py.csv')

# Identify suppression ratio columns
suppression_cols = [col for col in df1.columns if 'Suppression ratio' in col]  # Find all relevant columns

# Reshape DataFrame from wide to long format
df_long = df1.melt(id_vars=['Subj', 'Shock'], value_vars=suppression_cols,
                   var_name='Day', value_name='Suppression Ratio')

df_long['Day'] = df_long['Day'].str.strip() # Removes trailing or leading spaces 

df_long = df_long.dropna(subset=['Day'])  # Drop any NaN rows

# Extract day number
df_long['Day'] = df_long['Day'].str.extract('(\d+)').astype(int)

df_long['Suppression Ratio'] = pd.to_numeric(df_long['Suppression Ratio'], errors='coerce')  # Convert, setting errors to NaN

df2 = df_long.groupby(['Subj', 'Shock', 'Day']).mean(numeric_only=True).reset_index()

# Get list of unique subjects
subjects = df2['Subj'].unique()

# Create subplots (one for each subject)
fig, axes = plt.subplots(nrows=len(subjects), figsize=(8, len(subjects) * 4), sharex=True)

if len(subjects) == 1:
    axes = [axes]  # Ensure axes is iterable if only one subject

df2.rename(columns={'Shock': 'Cue paired with'}, inplace=True)

# Plot each subject separately
for ax, subj in zip(axes, subjects):
    sub_df = df2[df2['Subj'] == subj]  # Filter data for the subject
    

    sns.lineplot(data=sub_df, x='Day', y='Suppression Ratio', hue='Cue paired with', marker='o', ax=ax)
    
    # Add a horizontal dashed line at y = 0.5
    ax.axhline(y=0.5, color='gray', linestyle='dashed', linewidth=1)
    
    ax.set_title(f'Subject {subj}')
    ax.set_xlabel('Day')
    ax.set_ylabel('Mean Suppression Ratio')
    ax.set_ylim(-0.1,1.1)  # Ensure a consistent y-axis range across subjects
    ax.tick_params(axis='x', which='both', labelbottom=True)

plt.tight_layout()
plt.show()


##################################################################

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load the data
df1 = pd.read_csv(r'C:\Users\pturrent\Documents\Iordonova Lab\SPC pilot\Suppresion data for py.csv')
#df1 = pd.read_csv(r'C:\Users\pturrent\Documents\Iordonova Lab\SPC Ephys\Clean data for python\Part II\FC\Aggregated Suppresion data for py_CSV.csv')


# Identify suppression ratio columns
suppression_cols = [col for col in df1.columns if 'Suppression ratio' in col]  

# Reshape DataFrame from wide to long format
df_long = df1.melt(id_vars=['Subj', 'Shock', 'Shock 2'], value_vars=suppression_cols,
                   var_name='Day', value_name='Suppression Ratio')

df_long['Day'] = df_long['Day'].str.strip()  
df_long = df_long.dropna(subset=['Day'])  
df_long['Day'] = df_long['Day'].str.extract('(\d+)').astype(int)
df_long['Suppression Ratio'] = pd.to_numeric(df_long['Suppression Ratio'], errors='coerce')  

# Compute mean and standard error
df2 = df_long.groupby(['Subj', 'Shock', 'Day'])['Suppression Ratio'].agg(['mean', 'sem']).reset_index()
df2.rename(columns={'mean': 'Mean Suppression Ratio', 'sem': 'SEM', 'Shock': 'Cue paired with'}, inplace=True)

# Get unique subjects and days
subjects = df2['Subj'].unique()

# Get all days for consistent x-ticks
days = sorted(df2['Day'].unique()) 

# Dynamically adjust rows & columns

cols = 2  # 2 columns always

rows = -(-len(subjects) // cols)  # Ceiling division to ensure enough rows

# Create subplots
fig, axes = plt.subplots(nrows=rows, ncols=cols, figsize=(12, 4 * rows), sharex=True, sharey=True)
axes = np.array(axes).flatten()  # Flatten for easy indexing

# Plot each subject separately
for i, subj in enumerate(subjects):
    sub_df = df2[df2['Subj'] == subj]

    sns.lineplot(data=sub_df, x='Day', y='Mean Suppression Ratio', hue='Cue paired with',
                 marker='o', ax=axes[i], errorbar=None)

    # Add error bars
    for _, row in sub_df.iterrows():
        axes[i].errorbar(x=row['Day'], y=row['Mean Suppression Ratio'], yerr=row['SEM'],
                         fmt='none', capsize=5, color='black', alpha=0.7)

    # Add a horizontal dashed line at y = 0.5
    axes[i].axhline(y=0.5, color='gray', linestyle='dashed', linewidth=1)

    axes[i].set_title(f'Subject {subj}')
    axes[i].set_xlabel('Day')
    axes[i].set_ylabel('Mean Suppression Ratio')
    axes[i].set_ylim(-0.1, 1.1)

    # Ensure all x-axis have proper day labels
    axes[i].set_xticks(days)
    axes[i].set_xticklabels(days)

# Hide any unused subplots
for j in range(len(subjects), len(axes)):
    fig.delaxes(axes[j])  # Delete empty plots

plt.tight_layout()
plt.show()

############################### V3 ########################################################################################################################################

# Graphs the suppression ratios accross days for different subjects and corrects a mistake 
# from V2 where shock condition for day one repeats itself throughout all days

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import re

# Load the data
#df1 = pd.read_csv(r'C:\Users\pturrent\Documents\Iordonova Lab\SPC pilot\Suppresion data for py.csv')
#df1 = pd.read_csv(r'C:\Users\pturrent\Documents\Iordonova Lab\SPC-SOC Ephys 1\Clean data for python\Part II\FC\Aggregated Suppresion data for py_CSV.csv')
#df1 = pd.read_csv(r'C:\Users\pturrent\Documents\Iordonova Lab\SPC-SOC Ephys 1\Clean data for python\Supression data combined_CSV.csv')
#df1 = pd.read_csv(r'C:\Users\pturrent\Documents\Iordonova Lab\SPC-SOC Ephys 2\Data\Excel macro\FC suppression excel files\Supression data combined_CSV.csv')
#df1 = pd.read_csv(r'C:\Users\pturrent\Documents\Iordonova Lab\SPC-SOC pilot 2\Supression data combined_CSV.csv')


# SPC-SOC pilot 2

# Part 1 FC

# Part 2 FC
#df1 = pd.read_csv(r'C:\Users\pturrent\Documents\Iordonova Lab\SPC-SOC pilot 2\Supression data combined_CSV - Part II.csv')

#Part 2 Test 1
#df1 = pd.read_csv(r'C:\Users\pturrent\Documents\Iordonova Lab\SPC-SOC pilot 2\Excel files\2nd pilot part 2 test data for py avg baseline_CSV - Copy.csv')


#  SPC-SOC Ephys 3

#Part 1 FC
#df1 = pd.read_csv(r'C:\Users\pturrent\Documents\Iordonova Lab\SPC-SOC Ephys\SPC-SOC Ephys 3\Excel macro files\Supression data combined_CSV.csv')

# Part 2 FC
df1 = pd.read_csv(r'C:\Users\pturrent\Documents\Iordonova Lab\SPC-SOC Ephys\SPC-SOC Ephys 3\Excel macro files\Supression data combined_CSV - Part II.csv')



# Identify suppression ratio columns (e.g., 'Suppression ratio', 'Suppression ratio 2', etc.)
suppression_cols = [col for col in df1.columns if 'Suppression ratio' in col]

# Identify shock columns (e.g., 'Shock', 'Shock 2', 'Shock 3', etc.)
shock_cols = [col for col in df1.columns if col.startswith('Shock')]

# Melt the dataframe from wide to long format
df_long = df1.melt(
    id_vars=['Subj'] + shock_cols,
    value_vars=suppression_cols,
    var_name='Day',
    value_name='Suppression Ratio'
)

# Extract numeric day from suppression column names (default to 1 if no number)
df_long['Day Num'] = df_long['Day'].apply(
    lambda x: int(re.search(r'\d+', x).group()) if re.search(r'\d+', x) else 1
)

# Create a mapping from day number to shock column
day_to_shock_col = {i + 1: col for i, col in enumerate(shock_cols)}

# Map correct shock value for each row
df_long['Shock'] = df_long.apply(lambda row: row[day_to_shock_col[row['Day Num']]], axis=1)

# Drop old individual shock columns if you don't need them
df_long = df_long.drop(columns=shock_cols)


df_long['Day'] = df_long['Day'].str.strip()  
df_long = df_long.dropna(subset=['Day'])  
df_long['Day'] = df_long['Day'].str.extract('(\d+)').astype(int)
df_long['Suppression Ratio'] = pd.to_numeric(df_long['Suppression Ratio'], errors='coerce')  

# Compute mean and standard error
df2 = df_long.groupby(['Subj', 'Shock', 'Day'])['Suppression Ratio'].agg(['mean', 'sem']).reset_index()
df2.rename(columns={'mean': 'Mean Suppression Ratio', 'sem': 'SEM', 'Shock': 'Cue paired with'}, inplace=True)

df2['Cue paired with'] = df2['Cue paired with'].replace({
    'Shock': 'X+',
    'No shock': 'Y−'
})

# Get unique subjects and days
subjects = df2['Subj'].unique()

# Get all days for consistent x-ticks
days = sorted(df2['Day'].unique()) 

# Dynamically adjust rows & columns
cols = 4  # 2 columns always

rows = -(-len(subjects) // cols)  # Ceiling division to ensure enough rows

# Create subplots
fig, axes = plt.subplots(nrows=rows, ncols=cols, figsize=(16, 3 * rows), sharex=True, sharey=True)
axes = np.array(axes).flatten()  # Flatten for easy indexing

# Plot each subject separately
for i, subj in enumerate(subjects):
    sub_df = df2[df2['Subj'] == subj]

    sns.lineplot(data=sub_df,
                 x='Day', 
                 y='Mean Suppression Ratio', 
                 hue='Cue paired with',
                 marker='o',
                 palette={'X+': 'black', 'Y−': 'lightblue'}, 
                 ax=axes[i], 
                 errorbar=None)

    # Add error bars
    for _, row in sub_df.iterrows():
        axes[i].errorbar(x=row['Day'], y=row['Mean Suppression Ratio'], yerr=row['SEM'],
                         fmt='none', capsize=5, color='black', alpha=0.7)

    # Add a horizontal dashed line at y = 0.5
    axes[i].axhline(y=0.5, color='red', linestyle='dashed', linewidth=1)

    axes[i].set_title(f'Subject {subj}', fontsize=13, fontweight="bold", x=0.4, y=0.75)
    axes[i].set_xlabel('Day')
    axes[i].set_ylabel('Mean Suppression Ratio')
    axes[i].set_ylim(-0.1, 1.1)

    # Ensure all x-axis have proper day labels
    axes[i].set_xticks(days)
    axes[i].set_xticklabels(days)
    
for ax in axes:
    
    # Remove top/right box but keep x and y axis lines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)


for ax in axes:
    legend = ax.get_legend()
    if legend is not None:
        legend.set_title("")  # Remove title

# Hide any unused subplots
for j in range(len(subjects), len(axes)):
    fig.delaxes(axes[j])  # Delete empty plots

plt.tight_layout()
plt.show()

