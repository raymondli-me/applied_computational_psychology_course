# Module 1 Lab: Data Cleaning in Google Sheets

## Lab Overview
**Duration:** 60 minutes
**Tools Required:** Google Sheets (free with Google account)
**Dataset:** Andrea's Reddit Data (2,000 row sample - wedding conflicts from r/AmItheAsshole)

---

## Learning Goals
By the end of this lab, you will:
- Import a CSV file into Google Sheets from a URL
- Identify and remove missing values (NaN)
- Remove duplicate rows
- Standardize column headers
- Identify variable types
- Formulate a testable hypothesis

---

## Setup Instructions

### Step 1: Open Google Sheets
1. Go to [sheets.google.com](https://sheets.google.com)
2. Create a new blank spreadsheet
3. Name it "Module 1 - Data Cleaning Practice"

### Step 2: Import the Dataset from Course Data Bank

Google Sheets can import data directly from a URL. Use this link to Andrea's Reddit data (2,000 row sample):

```
https://storage.googleapis.com/variable-resolution-applied-computational-psychology-course/datasets/csv/andrea_sample_2k_for_sheets.csv
```

**To import:**
1. In Google Sheets: **File → Import**
2. Click the **"Upload"** tab, then click **"Browse"**
3. OR use **IMPORTDATA function** in cell A1:
   ```
   =IMPORTDATA("https://storage.googleapis.com/variable-resolution-applied-computational-psychology-course/datasets/csv/andrea_sample_2k_for_sheets.csv")
   ```

**Note:** This is a 2,000 row sample optimized for Google Sheets. The full dataset has 871K rows!

### Step 3: Initial Inspection
Before cleaning, ALWAYS look at your data first.

**Answer these questions:**
- How many rows are there? (Check bottom-left: "X rows")
- How many columns?
- What do the column headers say?
- Can you see any obvious problems?

---

## Understanding the Data

Andrea collected Reddit posts about wedding conflicts. Here's what each column means:

| Column | Description | Type |
|--------|-------------|------|
| Post Title | Title of the Reddit post | Text |
| Post URL | Link to the original post | Text (ID) |
| Post Score | Upvotes minus downvotes | Numeric |
| Post Author | Reddit username | Text (ID) |
| Post Num Comments | Number of comments | Numeric |
| Post Body | Full text of the post | Text |
| Post Created | When it was posted | Date/Time |
| Comment Body | A comment on the post | Text |
| Comment Score | Comment upvotes | Numeric |

---

## Cleaning Tasks

### Task 1: Understand Rows vs Columns (5 minutes)

**Key Concept: Tidy Data**
- Each **row** = one observation (in this case, one comment on a post)
- Each **column** = one variable (a property of that observation)

**Your Task:**
1. How many observations (rows) do you have?
2. How many variables (columns) do you have?
3. What is the "unit of analysis"? (What does each row represent?)

---

### Task 2: Identify Missing Values (15 minutes)

**Problem:** Some cells are empty or contain "NaN", "N/A", or blank values.

**Your Goal:** Find and document missing data patterns.

**Instructions:**

**Method 1: Visual Scan**
1. Scroll through the data
2. Look for empty cells, "NaN", or unusual values

**Method 2: Filter for Blanks**
1. Data → Create a filter
2. Click the filter icon on a column (e.g., "Comment Body")
3. Look for "(Blanks)" option - how many are there?

**Document your findings:**
| Column | Missing Values? | Notes |
|--------|-----------------|-------|
| Post Title | | |
| Post Body | | |
| Comment Body | | |
| Post Score | | |

**Question:** Why might "Comment Body" have missing values while "Post Title" doesn't?

---

### Task 3: Identify Variable Types (15 minutes)

**Your Goal:** Classify each column as a variable type.

Create a new sheet tab (click + at bottom) called "Variable_Types" and fill out:

| Column Name | Variable Type | Example Value |
|-------------|---------------|---------------|
| Post Title | Text (Unstructured) | "AITA for not inviting..." |
| Post Score | Continuous (Count) | 1523 |
| Post Author | Categorical (ID) | "username123" |
| Post Num Comments | Continuous (Count) | 87 |
| Post Created | Date/Time | 2024-11-19 |
| Comment Body | Text (Unstructured) | "NTA, your wedding your rules" |
| Comment Score | Continuous (Count) | 234 |

**Variable Type Definitions:**
- **Categorical (Nominal):** Categories with no order (e.g., username, subreddit)
- **Categorical (Ordinal):** Categories WITH order (e.g., rating: low/medium/high)
- **Continuous:** Numbers that can take any value (e.g., scores, counts)
- **Text (Unstructured):** Free-form text that needs processing

---

### Task 4: Spot Structured vs Unstructured Data (10 minutes)

**Key Insight for This Course:**

Some columns are **structured** (ready for analysis):
- Post Score (it's already a number!)
- Comment Score
- Post Num Comments

Some columns are **unstructured** (need processing):
- Post Body (raw text - how do you analyze this?)
- Comment Body (raw text)

**The Magic Question:** How do you turn "AITA for refusing to invite my sister to my wedding?" into a NUMBER you can analyze?

This is what the rest of the course teaches:
- Module 3: Use AI (LLMs) to rate the text
- Module 5: Convert text to embeddings (vectors of numbers)

**Your Task:** List 2 structured and 2 unstructured columns from this dataset.

---

### Task 5: Write Your Hypothesis (10 minutes)

Based on the variables available, write ONE testable hypothesis.

**Template:**
> "We predict that [INDEPENDENT VARIABLE] will [increase/decrease] [DEPENDENT VARIABLE]."

**Examples using this dataset:**
- "We predict that posts with more comments will have higher post scores."
- "We predict that longer post titles will receive more comments."
- "We predict that comments on high-scoring posts will also have high scores."

**Your Hypothesis:**
_________________________________

**Identify:**
- Independent Variable (IV): _____________
- Dependent Variable (DV): _____________

---

## Submission Checklist

### Required Deliverables:

1. **Screenshot 1:** Your data in Google Sheets (first 15 rows visible)
   - Show column headers clearly

2. **Screenshot 2:** Your "Variable_Types" tab

3. **Written Answers:**
   - How many rows/columns in your data?
   - Which columns are structured vs unstructured?
   - Your hypothesis with IV and DV labeled

---

## Troubleshooting

**"IMPORTDATA won't load"**
- Check the URL is exactly correct (copy-paste it)
- Try refreshing the page and re-entering the formula
- The 2K sample should load in under 30 seconds

**"My dates look weird (like 45678)"**
- Select the column → Format → Number → Date

**"I see a lot of NaN values"**
- That's part of the data - some posts don't have all fields
- Document which columns have missing data (that's the exercise!)

---

## Key Takeaways

Before moving to Module 2, make sure you understand:

1. **Rows = Observations, Columns = Variables**
2. **Structured data** (numbers) is ready to analyze
3. **Unstructured data** (text) needs processing first
4. **A hypothesis** links an IV to a DV with a predicted direction

---

## Next Steps

In **Module 2**, you'll learn to:
- Run linear regression on structured variables (like Post Score ~ Post Num Comments)
- Interpret coefficients and p-values
- This all happens in Python/Colab - no more Google Sheets!
