# Module 1 Lab: Data Cleaning in Google Sheets

## Lab Overview
**Duration:** 60 minutes
**Tools Required:** Google Sheets (free with Google account) or Google Colab
**Dataset:** Choose from the course dataset bank (see below)

---

## Dataset Options for This Lab

### Option A: Use Course Dataset Bank (Recommended)

Copy this boilerplate into a Colab notebook:
```python
# === DATASET LOADER (Run First) ===
import pandas as pd
import json
import urllib.request

GCS_BUCKET = "variable-resolution-applied-computational-psychology-course"
GCS_BASE_URL = f"https://storage.googleapis.com/{GCS_BUCKET}"
CATALOG_URL = f"{GCS_BASE_URL}/manifest.json"

# Load catalog
with urllib.request.urlopen(CATALOG_URL) as r:
    CATALOG = json.loads(r.read().decode())
print(f"Loaded catalog: {len(CATALOG['datasets'])} datasets available")

def load_dataset(name, nrows=None):
    """Load a dataset by name from GCS."""
    for ds in CATALOG['datasets']:
        if ds['canonical_name'] == name:
            url = ds['access']['public_url']
            df = pd.read_csv(url, nrows=nrows)
            print(f"Loaded {len(df):,} rows from {name}")
            return df
    raise ValueError(f"Dataset '{name}' not found")
```

Then load Andrea's wedding Reddit data:
```python
# Andrea's Wedding Reddit Data - 871,775 posts
# Perfect for Module 1: learning tidy data principles
df = load_dataset("andrea_reddit_results_andrea_2025_03_13", nrows=5000)  # Start with sample
df.head()
```

### Option B: Use Provided Sample
Download `youtube_comments_raw.csv` from the course Google Drive.

---

## Learning Goals
By the end of this lab, you will:
- Import a CSV file into Google Sheets
- Identify and remove missing values (NaN)
- Remove duplicate rows
- Standardize column headers
- Identify variable types

---

## Setup Instructions

### Step 1: Access the Dataset
1. Go to the course Google Drive folder
2. Download `youtube_comments_raw.csv`
3. Open Google Sheets (sheets.google.com)
4. File > Import > Upload > Select the CSV

### Step 2: Initial Inspection
Before cleaning, ALWAYS look at your data first.

**Answer these questions:**
- How many rows are there? (Check bottom-left: "X rows")
- How many columns?
- What do the column headers say?
- Can you see any obvious problems?

---

## Cleaning Tasks

### Task 1: Fix Column Headers (10 minutes)

**Problem:** The raw data has messy headers like "comment_txt", "VID_ID", "likes_count".

**Your Goal:** Standardize to snake_case and make them descriptive.

**Instructions:**
1. Click on row 1 (the header row)
2. Rename columns to:
   - `video_id`
   - `comment_text`
   - `like_count`
   - `reply_count`
   - `published_date`
   - `author_name`

**Why this matters:** Consistent naming prevents errors when you write code later.

---

### Task 2: Remove Missing Values (15 minutes)

**Problem:** Some cells are empty, contain "NaN", "N/A", or "#N/A".

**Your Goal:** Find and remove rows with critical missing data.

**Instructions:**

**Method 1: Find & Replace**
1. Edit > Find and replace (Ctrl/Cmd + H)
2. Find: `NaN`
3. Replace with: (leave empty)
4. Click "Replace all"
5. Repeat for: `N/A`, `#N/A`, `null`, `None`

**Method 2: Filter for Blanks**
1. Data > Create a filter
2. Click the filter icon on a column
3. Uncheck "Blanks" to hide empty rows
4. Select visible rows > Right-click > Delete rows

**Critical columns** (must have values):
- `video_id`
- `comment_text`

**Non-critical columns** (can be empty):
- `author_name`

---

### Task 3: Remove Duplicate Rows (10 minutes)

**Problem:** Some comments appear multiple times (scraped twice, API glitch, etc.)

**Your Goal:** Keep only unique comments.

**Instructions:**
1. Data > Data cleanup > Remove duplicates
2. Select columns to check: `video_id` AND `comment_text`
   - (Two comments are duplicates if they're on the same video with the same text)
3. Click "Remove duplicates"
4. Note how many were removed!

---

### Task 4: Identify Variable Types (15 minutes)

**Your Goal:** Classify each column as a variable type.

Fill out this table in a new sheet tab called "Variable_Types":

| Column Name | Variable Type | Notes |
|-------------|---------------|-------|
| video_id | Categorical (ID) | Unique identifier |
| comment_text | Text (Unstructured) | Will convert to ratings later |
| like_count | Continuous (Count) | Range: 0 to ? |
| reply_count | Continuous (Count) | Range: 0 to ? |
| published_date | Date/Time | Format: YYYY-MM-DD |
| author_name | Categorical (Nominal) | Could anonymize |

**Variable Type Definitions:**
- **Categorical (Nominal):** Categories with no order (e.g., video_id, author)
- **Categorical (Ordinal):** Categories with order (e.g., rating: low/medium/high)
- **Continuous:** Numbers that can take any value (e.g., like_count, sentiment score)
- **Text:** Unstructured text data

---

### Task 5: Write Your Hypothesis (10 minutes)

Based on the variables available, write ONE testable hypothesis.

**Template:**
> "We predict that [INDEPENDENT VARIABLE] will [increase/decrease] [DEPENDENT VARIABLE]."

**Examples using this dataset:**
- "We predict that comments with more likes will have more replies."
- "We predict that longer comments will receive more likes."
- "We predict that comments posted on weekends will receive fewer replies."

**Your Hypothesis:**
_________________________________

**Identify:**
- Independent Variable (IV): _____________
- Dependent Variable (DV): _____________

---

## Submission Checklist

### Required Deliverables:
1. **Screenshot 1:** Your cleaned data (first 20 rows visible)
   - Show that headers are standardized
   - Show no visible NaN values

2. **Screenshot 2:** Your "Variable_Types" tab

3. **Text Submission:**
   - Your hypothesis (1 sentence)
   - Your IV and DV

---

## Troubleshooting

**"I accidentally deleted too many rows!"**
- File > Version history > See version history
- Restore an earlier version

**"My dates look weird (like 45678)"**
- Select the column > Format > Number > Date

**"Find & Replace isn't finding my NaN values"**
- Check for spaces: try finding " NaN" or "NaN "
- Check for case: NaN vs nan vs NAN

---

## Challenge Extension (Optional)

**For students who finish early:**

1. Calculate basic statistics:
   - What's the average like_count?
   - What's the maximum reply_count?
   - How many unique video_ids are there?

2. Create a simple visualization:
   - Highlight column > Insert > Chart
   - Try a histogram of like_count

3. Identify potential outliers:
   - Are there comments with suspiciously high like counts?
   - Could these be bots or promotional content?
