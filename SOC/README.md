# 📊 Conditioned Suppression Plotting Script

## Overview 🧠

This script loads conditioned suppression behavioral data from a `.csv` file and generates subject-level visualizations of **suppression ratios across trials and trial blocks**.

It is designed for SPC / SOC experiments to allow:

- Trial-by-trial inspection of learning
- Comparison between cue types
- Quick evaluation of cohort quality before advancing stages

Each subject is plotted in a separate subplot for easy inspection.

---

## ⚙️ Dependencies:

 -pandas 
 -numpy 
 -matplotlib 
 -seaborn

The input CSV must include the following columns:

Column Name	Description
Subj	Subject identifier
Neutral	Cue category (C, D, X, Y)
Suppression Ratio	Suppression ratio per trial
Cue Meaning (experiment-specific)

X → First-order conditioned cue

C → Higher-order conditioned cue

D → Control cue

Y → Additional control cue

📌 Functions:



-------create_plots(data, categories, title_suffix)

Purpose:
Generates trial-by-trial line plots for each subject.

What it does:

-Filters selected cue categories

-Sorts data by subject and cue

-Reconstructs trial numbers

-Plots suppression ratio across trials

-Adds reference line at 0.5

Interpretation:

< 0.5 → conditioned suppression (learning)

≈ 0.5 → no representation transfer




-----create_bar_plots_trial_blocks(data, categories, title_suffix)

Purpose:
Creates bar plots of block-averaged suppression ratios.

Trial blocks:

Block	Trials
1–2	Early
3–4	Middle
5–6	Late

What it does:

-Assigns trials to blocks

-Averages suppression ratio per subject / cue / block

-Plots grouped bar charts



--------- create_line_plots_trial_blocks(data, categories, title_suffix)

Purpose:
Same as bar plots, but displayed as line plots.

Why use it:

Highlights learning trends

Easier to compare cue divergence

Better for visualizing higher-order conditioning effects

📐 Plot Layout

Subjects displayed in a 3-column grid

Rows adjust automatically

Empty plots are removed

Shared axes across subjects




## Overall :

The script will generate:

Trial-by-trial plots (all cues)

Conditioned cues only (X, C)

Control cues only (Y, D)

Bar plots (trial blocks)

Line plots (trial blocks)

⚠️ Important Notes

Assumes equal number of trials per cue

Missing trials may affect block averages

Cue labels must match exactly: C, D, X, Y

Designed for within-subject visualization, not group statistics
