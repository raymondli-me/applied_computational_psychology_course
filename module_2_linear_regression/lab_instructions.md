# Module 2 Lab: Your First Regression in Python

## Lab Overview
**Duration:** 60 minutes
**Tools Required:** Google Colab (free, browser-based Python)
**Dataset:** Choose from course dataset bank (see below)
**Notebook:** `01_regression_boilerplate.ipynb`

---

## Dataset Options for This Lab

### Recommended: Agatha's Dance Ratings
```python
# === DATASET LOADER (Run First) ===
import pandas as pd
import json
import urllib.request

GCS_BUCKET = "variable-resolution-applied-computational-psychology-course"
CATALOG_URL = f"https://storage.googleapis.com/{GCS_BUCKET}/manifest.json"

with urllib.request.urlopen(CATALOG_URL) as r:
    CATALOG = json.loads(r.read().decode())

def load_dataset(name, nrows=None):
    for ds in CATALOG['datasets']:
        if ds['canonical_name'] == name:
            url = ds['access']['public_url']
            return pd.read_csv(url, nrows=nrows)
    raise ValueError(f"Dataset '{name}' not found")

# Agatha's Dance Data - 30,511 posts with engagement scores
# Perfect for Module 2: regression with continuous variables
df = load_dataset("agatha_ballet_dancemoms_agatha", nrows=5000)
print(f"Loaded {len(df):,} rows with columns: {list(df.columns)}")
# Key columns: Post Score, Comment Score, Post Title, Post Num Comments
```

*Agatha's team of 6 human raters coded body image constructs in dance communities - ideal for inter-rater reliability practice.*

**Alternative datasets:** See `DATASETS_FOR_M2.md` for all options.

---

## Learning Goals
By the end of this lab, you will:
- Run a linear regression in Python using statsmodels
- Interpret the regression output
- Add control variables to your model
- Write up results in APA format

---

## Setup Instructions

### Step 1: Open Google Colab
1. Go to [colab.research.google.com](https://colab.research.google.com)
2. Sign in with your Google account
3. File > Open notebook > GitHub/Upload
4. Upload `01_regression_boilerplate.ipynb` from the course materials

### Step 2: Upload the Dataset
1. In Colab, click the folder icon (left sidebar)
2. Click the upload button
3. Upload `youtube_videos_clean.csv`

---

## Part 1: Understanding the Boilerplate (15 minutes)

The notebook has several cells. **Read the comments** before running each cell.

### Cell 1: Setup (Just Run It)
```python
# ============================================
# SETUP - Run this cell first, don't modify
# ============================================
import pandas as pd
import statsmodels.formula.api as smf
import warnings
warnings.filterwarnings('ignore')

# Load the data
df = pd.read_csv('youtube_videos_clean.csv')
print(f"Dataset loaded: {len(df)} videos")
print(f"Columns: {list(df.columns)}")
```

**What this does:** Imports libraries and loads your data.

### Cell 2: Explore the Data
```python
# ============================================
# EXPLORE - Look at your data
# ============================================
print("First 5 rows:")
print(df.head())

print("\nBasic statistics:")
print(df.describe())
```

**Your task:** Run this cell. Answer:
- What is the mean like_count?
- What is the range of word_count?

---

## Part 2: Simple Regression (20 minutes)

### Cell 3: Run Your First Regression
```python
# ============================================
# SIMPLE REGRESSION
# Predict: like_count (Y/DV)
# From: word_count (X/IV)
# ============================================

# Define the model using formula syntax
model = smf.ols('like_count ~ word_count', data=df)

# Fit the model
results = model.fit()

# Print the summary
print(results.summary())
```

**Your task:** Run this cell and find these three numbers:
1. The coefficient (coef) for word_count: ___________
2. The p-value (P>|t|) for word_count: ___________
3. The R-squared value: ___________

### Understanding the Output

**Look for this section in the output:**

```
                  coef    std err    t      P>|t|    [0.025    0.975]
-----------------------------------------------------------------------------
Intercept       XXX.XX    XXX.XX   X.XX    0.XXX    XXX.XX    XXX.XX
word_count        X.XX      X.XX   X.XX    0.XXX      X.XX      X.XX
```

- **coef:** This is the unstandardized coefficient (b)
- **P>|t|:** This is the p-value

**And this section:**
```
R-squared:           0.XXX
```

### Getting Standardized Beta (β)

To compare effects across variables, we need standardized coefficients:

```python
# ============================================
# STANDARDIZED COEFFICIENTS (BETA)
# ============================================
from scipy import stats

# Standardize variables (convert to z-scores)
df['word_count_z'] = stats.zscore(df['word_count'])
df['like_count_z'] = stats.zscore(df['like_count'])

# Run regression with standardized variables
model_std = smf.ols('like_count_z ~ word_count_z', data=df)
results_std = model_std.fit()

print("Standardized Beta (β):", round(results_std.params['word_count_z'], 3))
```

**Your task:** What is your standardized β? ___________

---

## Part 3: Multiple Regression (15 minutes)

Now let's control for view_count.

### Cell 4: Adding a Control Variable
```python
# ============================================
# MULTIPLE REGRESSION
# Predict: like_count (Y/DV)
# From: word_count (X1/IV) + view_count (Control)
# ============================================

# Add both predictors with +
model2 = smf.ols('like_count ~ word_count + view_count', data=df)
results2 = model2.fit()

print(results2.summary())
```

**Your task:** Compare results:

| | Simple Regression | Multiple Regression |
|--|---|---|
| β for word_count | ___ | ___ |
| p-value for word_count | ___ | ___ |
| R-squared | ___ | ___ |

**Interpretation question:** Did the effect of word_count get stronger, weaker, or stay the same after controlling for view_count? Why might this be?

---

## Part 4: Writing Your Results (10 minutes)

### Task: Write 3 APA-Style Sentences

Use this template:

**Sentence 1:** State what analysis you did
> "A [simple/multiple] linear regression was conducted to predict [DV] from [IV(s)]."

**Sentence 2:** Report the main finding
> "Results indicated that [IV] [significantly/did not significantly] predict [DV], β = [value], p [< .001 / = .XXX]."

**Sentence 3:** Report variance explained
> "The model explained [X]% of the variance in [DV] (R² = [value])."

### Your APA Write-Up:

**For Simple Regression:**
1. _______________________________________________
2. _______________________________________________
3. _______________________________________________

**For Multiple Regression (including "controlling for"):**
1. _______________________________________________
2. _______________________________________________
3. _______________________________________________

---

## Submission Checklist

### Required Deliverables:

1. **Screenshot:** Your regression output (the full summary table)

2. **Table:** Fill in these values

| Metric | Simple Regression | Multiple Regression |
|--------|-------------------|---------------------|
| β (word_count) | | |
| p-value | | |
| R² | | |

3. **APA Paragraph:** Your 3 sentences for the multiple regression

4. **Interpretation:** One sentence in plain language explaining what the results mean (e.g., "Videos with more words tend to get more likes, even accounting for how many views they got.")

---

## Troubleshooting

**"ModuleNotFoundError: No module named 'statsmodels'"**
- Run: `!pip install statsmodels` in a cell, then restart runtime

**"FileNotFoundError: youtube_videos_clean.csv"**
- Make sure you uploaded the file (check the folder icon)
- Check the filename matches exactly

**"My R² is really low (like 0.02)"**
- This is normal in psychology! Human behavior is messy
- An R² of 0.02 means 2% variance explained—small but can still be meaningful

**"My p-value is > .05"**
- That's also fine! It means the relationship isn't statistically significant
- Report it honestly: "did not significantly predict"

---

## Challenge Extension (Optional)

**For students who finish early:**

1. **Add another predictor:**
```python
model3 = smf.ols('like_count ~ word_count + view_count + comment_count', data=df)
```
How does R² change?

2. **Create a scatterplot:**
```python
import matplotlib.pyplot as plt
plt.scatter(df['word_count'], df['like_count'], alpha=0.5)
plt.xlabel('Word Count')
plt.ylabel('Like Count')
plt.title('Word Count vs. Likes')
plt.show()
```

3. **Check for non-linearity:** Does the relationship look linear, or is there a curve?
