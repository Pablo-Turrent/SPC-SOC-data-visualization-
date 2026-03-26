# Graphs the suppression ratios across trials for different subjects at test

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

#Pilot 2
#df1 = pd.read_csv(r'C:\Users\pturrent\Documents\Iordonova Lab\SPC-SOC pilot 2\2nd pilot test data for py avg baseline_CSV.csv')

#Ephys 3

#Part II

# SOC 1
#df1 = pd.read_csv(r'c:\Users\pturrent\Documents\Iordonova Lab\SPC-SOC Ephys\SPC-SOC Ephys 3\Excel macro files\Ephys 3 part 2 SOC 1 data for py avg baseline_CSV.csv')

# SOC 2
#df1 = pd.read_csv(r'C:\Users\pturrent\Documents\Iordonova Lab\SPC-SOC Ephys\SPC-SOC Ephys 3\Excel macro files\Ephys 3 part 2 SOC 2 data for py avg baseline_CSV.csv')


#Part III
# SOC 1
df1 = pd.read_csv(r'C:\Users\pturrent\Documents\Iordonova Lab\SPC-SOC Ephys\SPC-SOC Ephys 3\Excel macro files\Ephys 3 part 3 SOC 1 data for py avg baseline_CSV.csv')

#SOC 2
#df1 = pd.read_csv(r'C:\Users\pturrent\Documents\Iordonova Lab\SPC-SOC Ephys\SPC-SOC Ephys 3\Excel macro files\Ephys 3 part 3 SOC 2 data for py avg baseline_CSV.csv')


df2 = df1

# categorize each element shown in the column
df1['Neutral'] = pd.Categorical(df1['Neutral'], 
                                categories=['C', 'D', 'X', 'Y'],
                                ordered=True)

# Get unique subjects and days
subjects = df2['Subj'].unique()

# Define a function to create plots for specified categories
def create_plots(data, categories, title_suffix):
    # Filter for specified categories
    df_filtered = data[data['Neutral'].isin(categories)]
    
    # Sort the values according to subject and Neutral condition
    df_sorted = df_filtered.sort_values(['Subj', 'Neutral'])
    
    # Add a count column so that trial one matches the first trial of paired to the first trial of unpaired
    df_sorted['trial2'] = (
        df_sorted
        .groupby(['Subj', 'Neutral'])
        .cumcount() + 1
    )
    
    # Get all trials for consistent x-ticks
    trials = sorted(df_sorted['trial2'].unique())
    
    # Dynamically adjust rows & columns
    cols = 3
    rows = -(-len(subjects) // cols)  # Ceiling division
    
    # Create subplots
    fig, axes = plt.subplots(nrows=rows, ncols=cols, figsize=(10, 4 * rows), sharex=True, sharey=True)
    axes = np.array(axes).flatten()  # Flatten for easy indexing
    
    # Plot each subject separately
    for i, subj in enumerate(subjects):
        sub_df = df_sorted[df_sorted['Subj'] == subj]
        
        if len(sub_df) > 0:  # Only plot if subject has data
            sns.lineplot(
                data=sub_df,
                x='trial2',
                y='Suppression Ratio',
                hue='Neutral',
                style='Neutral',
                markers=True,
                dashes={'X': '', 'C': '', 'D': '', 'Y': ''},
                marker='o',
                errorbar=None,
                palette={'X': 'black', 'C': 'lightblue', 'D': 'purple', 'Y': 'lightgrey'},
                ax=axes[i]
            )
        
        # Add a horizontal dashed line at y = 0.5
        axes[i].axhline(y=0.5, color='red', linestyle='dashed', linewidth=1)
        
        axes[i].set_title(f'Subject {subj}', fontsize=13, fontweight="bold", x=0.6, y=0.75)
        axes[i].set_xlabel('Trial')
        axes[i].set_ylabel('Suppression Ratio')
        axes[i].set_ylim(-0.1, 1.1)
        
        # Ensure all x-axis have proper day labels
        if len(trials) > 0:
            axes[i].set_xticks(trials)
            axes[i].set_xticklabels(trials)
    
    # Format all axes
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
    
    fig.suptitle(f'Suppression Ratios - {title_suffix}', fontsize=16, fontweight='bold', y=0.995)
    plt.tight_layout()
    plt.show()

# Define a function to create bar plots comparing trial block averages
def create_bar_plots_trial_blocks(data, categories, title_suffix):
    # Filter for specified categories
    df_filtered = data[data['Neutral'].isin(categories)]
    
    # Add a count column to track trials per subject and neutral condition
    df_filtered = df_filtered.copy()
    df_filtered['trial2'] = (
        df_filtered
        .groupby(['Subj', 'Neutral'])
        .cumcount() + 1
    )
    
    # Define trial blocks: 1-2, 3-4, 5-6
    def assign_trial_block(trial):
        if trial in [1, 2]:
            return '1-2'
        elif trial in [3, 4]:
            return '3-4'
        elif trial in [5, 6]:
            return '5-6'
        else:
            return None
    
    df_filtered['trial_block'] = df_filtered['trial2'].apply(assign_trial_block)
    df_filtered = df_filtered.dropna(subset=['trial_block'])
    
    # Calculate average suppression ratio for each subject, category, and trial block
    df_avg = df_filtered.groupby(['Subj', 'Neutral', 'trial_block'])['Suppression Ratio'].mean().reset_index()
    
    # Remove unused categories from the Neutral column
    df_avg['Neutral'] = df_avg['Neutral'].cat.remove_unused_categories()
    
    # Dynamically adjust rows & columns
    cols = 3
    rows = -(-len(subjects) // cols)  # Ceiling division
    
    # Create subplots
    fig, axes = plt.subplots(nrows=rows, ncols=cols, figsize=(10, 4 * rows), sharex=True, sharey=True)
    axes = np.array(axes).flatten()  # Flatten for easy indexing
    
    # Plot each subject separately
    for i, subj in enumerate(subjects):
        sub_df = df_avg[df_avg['Subj'] == subj]
        
        if len(sub_df) > 0:  # Only plot if subject has data
            sns.barplot(
                data=sub_df,
                x='trial_block',
                y='Suppression Ratio',
                hue='Neutral',
                hue_order=[cat for cat in ['C', 'D', 'X', 'Y'] if cat in sub_df['Neutral'].unique()],
                palette={'C': 'lightblue', 'D': 'purple', 'X': 'black', 'Y': 'lightgrey'},
                ax=axes[i]
            )
        
        # Add a horizontal dashed line at y = 0.5
        axes[i].axhline(y=0.5, color='red', linestyle='dashed', linewidth=1)
        
        axes[i].set_title(f'Subject {subj}', fontsize=13, fontweight="bold", x=0.6, y=0.75)
        axes[i].set_xlabel('Trial Block')
        axes[i].set_ylabel('Average Suppression Ratio')
        axes[i].set_ylim(-0.1, 1.1)
    
    # Format all axes
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
    
    fig.suptitle(f'Suppression Ratios - {title_suffix}', fontsize=16, fontweight='bold', y=0.995)
    plt.tight_layout()
    plt.show()
    
    
def create_line_plots_trial_blocks(data, categories, title_suffix):
    # Filter for specified categories
    df_filtered = data[data['Neutral'].isin(categories)]
    
    # Add a count column to track trials per subject and neutral condition
    df_filtered = df_filtered.copy()
    df_filtered['trial2'] = (
        df_filtered
        .groupby(['Subj', 'Neutral'])
        .cumcount() + 1
    )
    
    # Define trial blocks: 1-2, 3-4, 5-6
    def assign_trial_block(trial):
        if trial in [1, 2]:
            return '1-2'
        elif trial in [3, 4]:
            return '3-4'
        elif trial in [5, 6]:
            return '5-6'
        else:
            return None
    
    df_filtered['trial_block'] = df_filtered['trial2'].apply(assign_trial_block)
    df_filtered = df_filtered.dropna(subset=['trial_block'])
    
    # Calculate average suppression ratio for each subject, category, and trial block
    df_avg = df_filtered.groupby(['Subj', 'Neutral', 'trial_block'])['Suppression Ratio'].mean().reset_index()
    
    # Remove unused categories from the Neutral column
    df_avg['Neutral'] = df_avg['Neutral'].cat.remove_unused_categories()
    
    # Dynamically adjust rows & columns
    cols = 3
    rows = -(-len(subjects) // cols)  # Ceiling division
    
    # Create subplots
    fig, axes = plt.subplots(nrows=rows, ncols=cols, figsize=(10, 4 * rows), sharex=True, sharey=True)
    axes = np.array(axes).flatten()  # Flatten for easy indexing
    
    # Plot each subject separately
    for i, subj in enumerate(subjects):
        sub_df = df_avg[df_avg['Subj'] == subj]
        
        if len(sub_df) > 0:  # Only plot if subject has data
            sns.lineplot(
                data=sub_df,
                x='trial_block',
                y='Suppression Ratio',
                hue='Neutral',
                marker='o',
                hue_order=[cat for cat in ['C', 'D', 'X', 'Y'] if cat in sub_df['Neutral'].unique()],
                palette={'C': 'lightblue', 'D': 'purple', 'X': 'black', 'Y': 'lightgrey'},
                ax=axes[i]
            )
        
        # Add a horizontal dashed line at y = 0.5
        axes[i].axhline(y=0.5, color='red', linestyle='dashed', linewidth=1)
        
        axes[i].set_title(f'Subject {subj}', fontsize=13, fontweight="bold", x=0.6, y=0.75)
        axes[i].set_xlabel('Trial Block')
        axes[i].set_ylabel('Average Suppression Ratio')
        axes[i].set_ylim(-0.1, 1.1)
    
    # Format all axes
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
    
    fig.suptitle(f'Suppression Ratios - {title_suffix}', fontsize=16, fontweight='bold', y=0.995)
    plt.tight_layout()
    plt.show()

# Generate all three plots
print("Generating plot 1: All categories (X, Y, C, D)...")
create_plots(df2, ['X', 'Y', 'C', 'D'], "All Cues" )

print("Generating plot 2: X and C only...")
create_plots(df2, ['X', 'C'], "First order and High order cues")

print("Generating plot 3: Y and D only...")
create_plots(df2, ['Y', 'D'], "Control cues")

print("Generating plot 4: C and D trial block averages...")
create_bar_plots_trial_blocks(df2, ['C', 'D'], "C and D Trial Block Averages")

print("Generating plot 5: C and D trial block averages...")
create_line_plots_trial_blocks(df2, ['C', 'D'], "C and D Trial Block Averages")

