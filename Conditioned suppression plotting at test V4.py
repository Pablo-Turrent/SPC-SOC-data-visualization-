# -*- coding: utf-8 -*-
"""
Created on Fri Mar 14 09:22:20 2025

@author: pturrent
"""

##########################################################################

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from scipy.stats import shapiro, ttest_rel, mannwhitneyu
from scipy import stats

# Load the dataset

#Pilot 
#df_neutral = pd.read_csv(r'C:\Users\pturrent\Documents\Iordonova Lab\SPC-SOC pilot\Test\Test data for py_CSV 10 base .csv')
#df_neutral = pd.read_csv(r'C:\Users\pturrent\Documents\Iordonova Lab\SPC-SOC pilot\Test\Test 2 data for py CSV.csv')
#df_neutral = pd.read_csv(r'C:\Users\pturrent\Documents\Iordonova Lab\SPC-SOC pilot\Test\Test data for py avg_baseline_CSV.csv')
#df_neutral = pd.read_csv(r'C:\Users\pturrent\Documents\Iordonova Lab\SPC-SOC pilot\Test\Test 2 data for py avg baseline CSV.csv')
#df_neutral = pd.read_csv(r'C:\Users\pturrent\Documents\Iordonova Lab\SPC-SOC pilot\Test\Test data for py full ITI_CSV.csv')
#df_neutral = pd.read_csv(r'C:\Users\pturrent\Documents\Iordonova Lab\SPC-SOC pilot\Test\Test data for py_CSV.csv')
#df_neutral = pd.read_csv(r'C:\Users\pturrent\Documents\Iordonova Lab\SPC-SOC pilot\Test\Test data for py avg_baseline_CSV.csv')


#Ephys 1
#df_neutral = pd.read_csv(r'C:\Users\pturrent\Documents\Iordonova Lab\SPC-SOC Ephys 1\Clean data for python\Test\2nd exp test data for py_CSV.csv')
#df_neutral = pd.read_csv(r'C:\Users\pturrent\Documents\Iordonova Lab\SPC-SOC Ephys 1\Clean data for python\Test\2nd exp 2nd test data for py_CSV.csv')
#df_neutral = pd.read_csv(r'C:\Users\pturrent\Documents\Iordonova Lab\SPC-SOC Ephys 1\Clean data for python\Part II\Test\2nd exp Part II Test-1 data for py_CSV.csv')
#df_neutral = pd.read_csv(r'C:\Users\pturrent\Documents\Iordonova Lab\SPC-SOC Ephys 1\Clean data for python\Part II\Test\2nd exp Part II Test-2 data for py_CSV.csv')
#df_neutral = pd.read_csv(r'C:\Users\pturrent\Documents\Iordonova Lab\SPC-SOC Ephys 1\Clean data for python\Test\2nd exp test data for py avg baseline_CSV.csv')
#df_neutral = pd.read_csv(r'C:\Users\pturrent\Documents\Iordonova Lab\SPC-SOC Ephys 1\Clean data for python\Test\2nd exp 2nd test data for py avg baseline_CSV - Copy.csv')
#df_neutral = pd.read_csv(r'C:\Users\pturrent\Documents\Iordonova Lab\SPC-SOC Ephys 1\Clean data for python\Test\2nd exp test data for py full ITI_CSV.csv')


#Ephys 2
#df_neutral = pd.read_csv(r'C:\Users\pturrent\Documents\Iordonova Lab\SPC-SOC Ephys 2\Data\Test\3rd exp test data for py_CSV.csv')
#df_neutral = pd.read_csv(r'C:\Users\pturrent\Documents\Iordonova Lab\SPC-SOC Ephys 2\Data\Test\3rd exp 2nd test data for py_CSV.csv')
#df_neutral = pd.read_csv(r'C:\Users\pturrent\Documents\Iordonova Lab\SPC-SOC Ephys 2\Data\Part II\Test\2nd exp phase II test data for py_CSV.csv')
#df_neutral = pd.read_csv(r'C:\Users\pturrent\Documents\Iordonova Lab\SPC-SOC Ephys 2\Data\Part II\Test\2nd exp phase II 2nd test data for py_CSV.csv')
#df_neutral = pd.read_csv(r'C:\Users\pturrent\Documents\Iordonova Lab\SPC-SOC Ephys 2\Data\Test\3rd exp test data for py_CSV.csv')
#df_neutral = pd.read_csv(r'C:\Users\pturrent\Documents\Iordonova Lab\SPC-SOC Ephys 2\Data\Test\3rd exp 2nd test data for py_CSV.csv')
#df_neutral = pd.read_csv(r'C:\Users\pturrent\Documents\Iordonova Lab\SPC-SOC Ephys 2\Data\Test\3rd exp test data for py avg baseline_CSV.csv')
#df_neutral = pd.read_csv(r'C:\Users\pturrent\Documents\Iordonova Lab\SPC-SOC Ephys 2\Data\Test\3rd exp 2nd test data for py avg baseline_CSV.csv')
#df_neutral = pd.read_csv(r'C:\Users\pturrent\Documents\Iordonova Lab\SPC-SOC Ephys 2\Data\Test\3rd exp test data for py full ITI_CSV.csv')

#Pilot 2
#df_neutral = pd.read_csv(r'C:\Users\pturrent\Documents\Iordonova Lab\SPC-SOC pilot 2\2nd pilot test data for py avg baseline_CSV.csv')
#df_neutral = pd.read_csv(r'C:\Users\pturrent\Documents\Iordonova Lab\SPC-SOC pilot 2\2nd pilot SPC 2nd test data for py avg baseline_CSV - Copy.csv')
#SOC Test 1
#df_neutral = pd.read_csv(r'C:\Users\pturrent\Documents\Iordonova Lab\SPC-SOC pilot 2\Excel files\2nd pilot part 2 test data for py avg baseline_CSV - Copy.csv')
#SOC Test 2
#df_neutral = pd.read_csv(r'C:\Users\pturrent\Documents\Iordonova Lab\SPC-SOC pilot 2\Excel files\2nd pilot part 2 2nd test data for py avg baseline_CSV.csv')


# Ephys 3

# SPC Test 1
#df_neutral = pd.read_csv(r'C:\Users\pturrent\Documents\Iordonova Lab\SPC-SOC Ephys\SPC-SOC Ephys 3\Excel macro files\Ephys 3 part 1 test data for py avg baseline_CSV - Copy.csv')

# SPC Test 2
#df_neutral = pd.read_csv(r'C:\Users\pturrent\Documents\Iordonova Lab\SPC-SOC Ephys\SPC-SOC Ephys 3\Excel macro files\Ephys 3 SPC 2nd test data for py avg baseline_CSV - Copy.csv')

#SOC Test 1
df_neutral = pd.read_csv(r'C:\Users\pturrent\Documents\Iordonova Lab\SPC-SOC Ephys\SPC-SOC Ephys 3\Excel macro files\Ephys 3 part 2 test data for py avg baseline_CSV.csv')






df_neutral["Neutral"] = pd.Categorical(
    df_neutral["Neutral"],
    categories=["Paired", "Unpaired"],
    ordered=True
)


# Create bar plot for Neutral vs. No Neutral conditions
plt.figure(figsize=(12, 8))
sns.barplot(
    data=df_neutral, 
    x="Subj", 
    y="Suppression Ratio", 
    hue="Neutral", 
    palette={'Paired': 'black', 'Unpaired': 'lightgrey'},  
    errorbar=None
)


# Labels and title
plt.xlabel("Subject")
plt.ylabel("Mean Suppression Ratio")
plt.title("Average Suppression Ratios for Paired & Unpaired Cues (TEST II, All rats)")
plt.ylim(0, 1)  # Keep y-axis range consistent
plt.legend(title="Condition")
plt.grid(axis="y", linestyle="--", alpha=0.7)

plt.axhline(0.5, color='red', linestyle='--', linewidth=1.5)

# Show plot
plt.show()

# Step 1: Compute mean suppression ratio per Subject & Condition**
df_mean = df_neutral.groupby(['Subj', 'Neutral'])['Suppression Ratio'].mean().unstack()

df_mean2 = df_neutral.groupby(['Neutral']).mean()

# Step 2: Extract matched pairs for the paired t-test**
paired = df_mean['Paired']  # Suppression ratios for the "Paired" condition
unpaired = df_mean['Unpaired']  # Suppression ratios for the "Unpaired" condition

# Step 3: Check normality of paired differences
diffs = paired - unpaired
shapiro_diff_p = shapiro(diffs).pvalue
sorted_diffs = diffs.sort_values()
sorted_paired = paired.sort_values()
sorted_unpaired = unpaired.sort_values()

# Step 4: Perform Paired t-test**
t_stat, p_ttest = ttest_rel(paired, unpaired, nan_policy='omit')  # 'omit' ignores NaN values

# Step 5: Perform Mann-Whitney U test (if normality is violated)**
u_stat, p_mwu = mannwhitneyu(paired, unpaired, alternative='two-sided')


#  To perform an Independent T-test 

# Split data by condition
paired = df_neutral[df_neutral['Neutral'] == 'Paired']['Suppression Ratio']
unpaired = df_neutral[df_neutral['Neutral'] == 'Unpaired']['Suppression Ratio']

# Compute Shapiro test for normality of the two conditions 
shap1 = shapiro(unpaired).pvalue
shap2 = shapiro(paired).pvalue



# **Print Results**
print("Unpaired Condition Normality: p = ", shapiro(unpaired).pvalue)
print("Paired Condition Normality: p = ", shapiro(paired).pvalue)

# **Interpretation**
if shapiro_diff_p < 0.05:
    print("Differences are NOT normally distributed → Use Mann-Whitney U test.")
    print(f"Mann-Whitney U test results: U = {u_stat:.3f}, p = {p_mwu:.3f}")
else:
    print("Differences are normally distributed → Paired t-test is appropriate.")
    print(f"Normality test: p = {shapiro_diff_p:.3f}")
    print(f"Paired t-test results: t = {t_stat:.3f}, p = {p_ttest:.3f}")



# Specify the subject to exclude
exclude_subj = 7
#exclude_subj2 = 7  

# Filter out the subject
df_filtered = df_neutral[df_neutral['Subj'] != exclude_subj]

#df_filtered = df_filtered[df_filtered['Subj'] != exclude_subj2]


# **Recompute the mean suppression ratio per Subject & Condition**
df_mean_filtered = df_filtered.groupby(['Subj', 'Neutral'])['Suppression Ratio'].mean().unstack()

# **Extract matched pairs for the paired t-test**
paired = df_mean_filtered['Paired']  # Suppression ratios for "Paired" condition
unpaired = df_mean_filtered['Unpaired']  # Suppression ratios for "Unpaired" condition

# **Perform Paired t-test**
t_stat, p_ttest = stats.ttest_rel(paired, unpaired, nan_policy='omit')  # 'omit' ignores NaN values

# **Print Results**
#print(f"Paired t-test results (excluding Subjects {exclude_subj} & {exclude_subj2}): t = {t_stat:.3f}, p = {p_ttest:.3f}")
print(f"Paired t-test results (excluding Subjects {exclude_subj}: t = {t_stat:.3f}, p = {p_ttest:.3f}")



    
############################################## For plotting nose poke numbers during pre-cues & actual cues ############################################### 

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

#df_1 = pd.read_csv(r'C:\Users\pturrent\Documents\Iordonova Lab\SPC-SOC Ephys 2\Data\Part II\Test\2nd exp test data for py_CSV.csv')
#df_1 = pd.read_csv(r'C:\Users\pturrent\Documents\Iordonova Lab\SPC-SOC Ephys 2\Data\Part II\Test\2nd exp phase II 2nd test data for py_CSV.csv')
df_1 = pd.read_csv(r'C:\Users\pturrent\Documents\Iordonova Lab\SPC-SOC Ephys 2\Data\Part II\Test\2nd exp phase II test data NP numbers for py_CSV - Copy.csv')
                   
df_2 = df_1
df_2['Trial 2'] = 1
            
b = 1
d = 1
e = 0

for i, val in enumerate(df_1['Neutral']):
    if val == 'Paired':
        df_2.loc[e, 'Trial 2'] = b
        b += 1
    elif val == 'Unpaired':
        df_2.loc[e, 'Trial 2'] = d
        d += 1
    e += 1



grouped_dfs = {}

for subj, sub_df in df_2.groupby('Subj'):
    grouped_dfs[subj] = sub_df
    
df_subj_1 = grouped_dfs[1]
#df_subj_2 = grouped_dfs[3]

for key, val in grouped_dfs.items():
    
    plt.figure(figsize=(12, 8))
    sns.barplot(
        data=val, 
        x="Trial 2", 
        y="NP", 
        hue= "Neutral", 
        palette=["lightblue", "black"],  
        errorbar=None
    )
    
    
    # Labels and title
    plt.xlabel("Trial number")
    plt.ylabel("Suppression Ratio")
    plt.title("Suppression Ratios for Paired & Unpaired Cues (TEST I)")
    plt.ylim(0, 6)  # Keep y-axis range consistent
    plt.legend(title="Condition")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    
    
    # Show plot
    plt.show()
