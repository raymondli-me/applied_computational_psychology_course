# Module 2 Lab: Your First Regression in Python

## Lab Overview
**Duration:** 60 minutes
**Tools Required:** Google Colab (free, browser-based Python)
**Dataset:** Agatha's Dance Community Data (from course dataset bank)

---

## Learning Goals
By the end of this lab, you will:
- Run a linear regression in Python using statsmodels
- Interpret the regression output (β, p-value, R²)
- Add control variables to your model
- Write up results in APA format

---

## Setup Instructions

### Step 1: Open the Course Notebook
1. Go to the course repository on GitHub
2. Click the "Open in Colab" badge
3. If you haven't already, save a copy to your Drive (File → Save a copy in Drive)

### Step 2: Load the Dataset
Run the setup cell first (if you haven't already this session), then load Agatha's data:

```python
# Load Agatha's Dance Community Data
df = load_dataset("agatha_ballet_dancemoms_agatha")
print(f"Loaded {len(df):,} rows")
print(f"Columns: {list(df.columns)}")
df.head()
```

**About this dataset:** Agatha collected posts from dance communities (ballet, DanceMoms, etc.) to study body image discussions. Key columns:
- `Post Score` - upvotes/engagement (our DV)
- `Post Num Comments` - number of comments
- `Post Title` - title text (we can compute length)

---

## Part 1: Explore the Data (10 minutes)

Before running any analysis, understand what you're working with.

```python
# Basic exploration
print("Dataset shape:", df.shape)
print("\nColumn types:")
print(df.dtypes)

print("\nBasic statistics for numeric columns:")
print(df.describe())
```

**Your task:** Answer these questions:
1. How many rows (observations)?
2. How many columns (variables)?
3. What is the mean Post Score?
4. What is the range of Post Num Comments?

---

## Part 2: Simple Regression (20 minutes)

Let's predict Post Score from the number of comments.

### Step 1: Import statsmodels and run regression

```python
import statsmodels.formula.api as smf

# Simple regression: Does number of comments predict post score?
model = smf.ols('Q("Post Score") ~ Q("Post Num Comments")', data=df)
results = model.fit()
print(results.summary())
```

**Note:** We use `Q("Column Name")` when column names have spaces.

### Step 2: Find these key values in the output

Look for this section:
```
                         coef    std err    t      P>|t|    [0.025    0.975]
----------------------------------------------------------------------------------
Intercept              XXX.XX    XXX.XX   X.XX    0.XXX    XXX.XX    XXX.XX
Q("Post Num Comments")   X.XX      X.XX   X.XX    0.XXX      X.XX      X.XX
```

**Your task:** Record these values:
1. Coefficient for Post Num Comments: ___________
2. P-value for Post Num Comments: ___________
3. R-squared (find at top of output): ___________

### Step 3: Interpret the results

- **Coefficient (coef):** For each additional comment, Post Score changes by this amount
- **P-value (P>|t|):** If < .05, the relationship is statistically significant
- **R-squared:** Proportion of variance in Post Score explained by the model

---

## Part 3: Create a Predictor Variable (10 minutes)

Let's test if title length predicts engagement.

```python
# Create a new variable: title length
df['title_length'] = df['Post Title'].fillna('').str.len()

print("Title length stats:")
print(df['title_length'].describe())
```

Now run regression with title length:

```python
# Does title length predict post score?
model2 = smf.ols('Q("Post Score") ~ title_length', data=df)
results2 = model2.fit()
print(results2.summary())
```

**Your task:**
1. What is the coefficient for title_length? ___________
2. Is it significant (p < .05)? ___________
3. What does this mean in plain language?

---

## Part 4: Multiple Regression (15 minutes)

Now let's control for one variable while testing another.

```python
# Multiple regression: title_length + Post Num Comments
model3 = smf.ols('Q("Post Score") ~ title_length + Q("Post Num Comments")', data=df)
results3 = model3.fit()
print(results3.summary())
```

**Your task:** Compare results:

| Metric | Simple (title only) | Multiple (both) |
|--------|---------------------|-----------------|
| β for title_length | ___ | ___ |
| p-value for title_length | ___ | ___ |
| R-squared | ___ | ___ |

**Interpretation question:** Did the effect of title_length change after controlling for Post Num Comments? Why might this be?

---

## Part 5: Getting Standardized Beta (β)

To compare effects across variables with different scales, use standardized coefficients:

```python
from scipy import stats

# Standardize variables (convert to z-scores)
df['post_score_z'] = stats.zscore(df['Post Score'].fillna(0))
df['title_length_z'] = stats.zscore(df['title_length'].fillna(0))
df['num_comments_z'] = stats.zscore(df['Post Num Comments'].fillna(0))

# Run regression with standardized variables
model_std = smf.ols('post_score_z ~ title_length_z + num_comments_z', data=df)
results_std = model_std.fit()

print("Standardized Betas:")
print(f"  title_length: β = {results_std.params['title_length_z']:.3f}")
print(f"  num_comments: β = {results_std.params['num_comments_z']:.3f}")
```

**Your task:** Which variable has a stronger effect on Post Score?

---

## Part 6: Write Your Results in APA Format (5 minutes)

Use this template:

**Sentence 1:** State what analysis you did
> "A multiple linear regression was conducted to predict [DV] from [IV1] and [IV2]."

**Sentence 2:** Report the main finding
> "Results indicated that [IV] [significantly/did not significantly] predicted [DV], β = [value], p [< .001 / = .XXX]."

**Sentence 3:** Report variance explained
> "The model explained [X]% of the variance in [DV] (R² = [value])."

**Your APA Write-Up:**
1. _______________________________________________
2. _______________________________________________
3. _______________________________________________

---

## Submission Checklist

### Required Deliverables:

1. **Screenshot:** Your multiple regression output

2. **Table:** Fill in these values

| Metric | Simple Regression | Multiple Regression |
|--------|-------------------|---------------------|
| β (title_length) | | |
| p-value | | |
| R² | | |

3. **APA Paragraph:** Your 3 sentences for the multiple regression

4. **Plain Language:** One sentence explaining what the results mean

---

## Troubleshooting

**"ModuleNotFoundError: No module named 'statsmodels'"**
```python
!pip install statsmodels
```
Then restart runtime (Runtime → Restart runtime)

**"KeyError: 'Post Score'"**
- Check column names with `print(df.columns)`
- Column names are case-sensitive

**"My R² is really low (like 0.02)"**
- This is normal in psychology! Human behavior is messy
- An R² of 0.02 means 2% variance explained—small but can still be meaningful

**"My p-value is > .05"**
- That's also fine! It means the relationship isn't statistically significant
- Report it honestly: "did not significantly predict"

---

## Key Takeaways

Before moving to Module 3, make sure you understand:

1. **Regression predicts** a DV from one or more IVs
2. **Coefficient (β)** tells you direction and strength of relationship
3. **P-value** tells you if the relationship is statistically significant
4. **R²** tells you how much variance is explained
5. **Controlling for** a variable means including it in the model
