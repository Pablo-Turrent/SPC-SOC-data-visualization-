# -*- coding: utf-8 -*-
"""
Created on Tue Mar 11 15:44:44 2025

@author: pturrent
"""


# Graphs the suppression ratios accross trials for different subjects at test

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import re

# Load the data

#Pilot
#df1 = pd.read_csv(r'C:\Users\pturrent\Documents\Iordonova Lab\SPC-SOC pilot\Test\Test data for py_CSV.csv')
#df1 = pd.read_csv(r'C:\Users\pturrent\Documents\Iordonova Lab\SPC-SOC pilot\Test\Test 2 data for py CSV.csv')
#df1 = pd.read_csv(r'C:\Users\pturrent\Documents\Iordonova Lab\SPC-SOC pilot\Test\Test data for py avg_baseline_CSV.csv')
#df1 = pd.read_csv(r'C:\Users\pturrent\Documents\Iordonova Lab\SPC-SOC pilot\Test\Test 2 data for py avg baseline CSV.csv')

#Pilot 2
#SOC Test 1
#df1 = pd.read_csv(r'C:\Users\pturrent\Documents\Iordonova Lab\SPC-SOC pilot 2\Excel files\2nd pilot part 2 test data for py avg baseline_CSV - Copy.csv')
#SOC Test 2
#df1 = pd.read_csv(r'C:\Users\pturrent\Documents\Iordonova Lab\SPC-SOC pilot 2\Excel files\2nd pilot part 2 2nd test data for py avg baseline_CSV.csv')




#Ephys 1
#df1 = pd.read_csv(r'C:\Users\pturrent\Documents\Iordonova Lab\SPC-SOC Ephys 1\Clean data for python\Test\2nd exp test data for py_CSV.csv')
#df1 = pd.read_csv(r'C:\Users\pturrent\Documents\Iordonova Lab\SPC-SOC Ephys 1\Clean data for python\Test\2nd exp 2nd test data for py_CSV.csv')
#df1 = pd.read_csv(r'C:\Users\pturrent\Documents\Iordonova Lab\SPC-SOC Ephys 1\Clean data for python\Part II\Test\2nd exp Part II Test-1 data for py_CSV.csv')
#df1 = pd.read_csv(r'C:\Users\pturrent\Documents\Iordonova Lab\SPC-SOC Ephys 1\Clean data for python\Part II\Test\2nd exp Part II Test-2 data for py_CSV.csv')
#df1 = pd.read_csv(r'C:\Users\pturrent\Documents\Iordonova Lab\SPC-SOC Ephys 1\Clean data for python\Test\2nd exp test data for py avg baseline_CSV.csv')
#df1 = pd.read_csv(r'C:\Users\pturrent\Documents\Iordonova Lab\SPC-SOC Ephys 1\Clean data for python\Test\2nd exp 2nd test data for py avg baseline_CSV - Copy.csv')


#Ephys 2
#df1 = pd.read_csv(r'C:\Users\pturrent\Documents\Iordonova Lab\SPC-SOC Ephys 2\Data\Test\3rd exp test data for py_CSV.csv')
#df1 = pd.read_csv(r'C:\Users\pturrent\Documents\Iordonova Lab\SPC-SOC Ephys 2\Data\Test\3rd exp 2nd test data for py_CSV.csv')
#df1 = pd.read_csv(r'C:\Users\pturrent\Documents\Iordonova Lab\SPC-SOC Ephys 2\Data\Part II\Test\2nd exp phase II test data for py_CSV.csv')
#df1 = pd.read_csv(r'C:\Users\pturrent\Documents\Iordonova Lab\SPC-SOC Ephys 2\Data\Part II\Test\2nd exp phase II 2nd test data for py_CSV.csv')
#df1 = pd.read_csv(r'C:\Users\pturrent\Documents\Iordonova Lab\SPC-SOC Ephys 2\Data\Test\3rd exp test data for py avg baseline_CSV.csv')
#df1 = pd.read_csv(r'C:\Users\pturrent\Documents\Iordonova Lab\SPC-SOC Ephys 2\Data\Test\3rd exp 2nd test data for py avg baseline_CSV.csv')

#Ephys 3

#SPC
# Test 1
#df1 = pd.read_csv(r'C:\Users\pturrent\Documents\Iordonova Lab\SPC-SOC Ephys\SPC-SOC Ephys 3\Excel macro files\Ephys 3 part 1 test data for py avg baseline_CSV - Copy.csv')

# Test 2
#df1 = pd.read_csv(r'C:\Users\pturrent\Documents\Iordonova Lab\SPC-SOC Ephys\SPC-SOC Ephys 3\Excel macro files\Ephys 3 SPC 2nd test data for py avg baseline_CSV - Copy.csv')

#SOC
# Test 1
df1 = pd.read_csv(r'C:\Users\pturrent\Documents\Iordonova Lab\SPC-SOC Ephys\SPC-SOC Ephys 3\Excel macro files\Ephys 3 part 2 test data for py avg baseline_CSV.csv')


 
df2 = df1

# categorize each element shown in the column
df1['Neutral'] = pd.Categorical(df1['Neutral'], 
                                categories=['Paired', 'Unpaired'],
                                ordered=True)

# sort the values acording to subject and Neutral condition
df_sorted = df1.sort_values(['Subj', 'Neutral'])

# Get unique subjects and days
subjects = df2['Subj'].unique()

#add a count column so that trial one matches the first trial of paired to the first trial of unpaired 
df_sorted['trial2'] = (
    df_sorted
    .groupby(['Subj', 'Neutral'])
    .cumcount() + 1
)

# Get all days for consistent x-ticks
trials = sorted(df_sorted['trial2'].unique()) 

# Dynamically adjust rows & columns
cols = 4  # 2 columns always

rows = -(-len(subjects) // cols)  # Ceiling division to ensure enough rows

# Create subplots
fig, axes = plt.subplots(nrows=rows, ncols=cols, figsize=(20, 4 * rows), sharex=True, sharey=True)
axes = np.array(axes).flatten()  # Flatten for easy indexing

# Plot each subject separately
for i, subj in enumerate(subjects):
    sub_df = df_sorted[df_sorted['Subj'] == subj]

    sns.lineplot(
    data=sub_df,
    x='trial2',
    y='Suppression Ratio',
    hue='Neutral',
    style='Neutral',                     
    markers=True,
    dashes={'Paired': '', 'Unpaired': (2,2)},   # ← Line styles (solid vs dashed)
    marker='o',
    errorbar=None,
    palette={'Paired': 'black', 'Unpaired': 'lightgrey'},
    ax=axes[i]
)


    # Add a horizontal dashed line at y = 0.5
    axes[i].axhline(y=0.5, color='red', linestyle='dashed', linewidth=1)

    axes[i].set_title(f'Subject {subj}', fontsize=13, fontweight="bold", x=0.6, y=0.75)
    axes[i].set_xlabel('Trial')
    axes[i].set_ylabel('Suppression Ratio')
    axes[i].set_ylim(-0.1, 1.1)

    # Ensure all x-axis have proper day labels
    axes[i].set_xticks(trials)
    axes[i].set_xticklabels(trials)
    
    
for ax in axes:
    
    # Remove top/right box but keep x and y axis lines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    legend = ax.get_legend()
    if legend is not None:
        legend.set_title("")  # Remove title

# Hide any unused subplots
for j in range(len(subjects), len(axes)):
    fig.delaxes(axes[j])  # Delete empty plots

plt.tight_layout()
plt.show()