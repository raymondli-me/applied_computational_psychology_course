# Module 4 Lab: Collecting Your Own Dataset

## Lab Overview
**Duration:** 60 minutes
**Tools Required:** Google Colab, API access (provided)
**Notebook:** `03_data_collection_boilerplate.ipynb`

---

## Study These Exemplar Collections First

Before collecting your own data, study how past students designed their collection strategies:

### Elle's YouTube Channel Collection (Exemplar)
```python
# === DATASET LOADER ===
import pandas as pd, json, urllib.request
GCS_BUCKET = "variable-resolution-applied-computational-psychology-course"
CATALOG_URL = f"https://storage.googleapis.com/{GCS_BUCKET}/manifest.json"
with urllib.request.urlopen(CATALOG_URL) as r:
    CATALOG = json.loads(r.read().decode())

def load_dataset(name, nrows=None):
    for ds in CATALOG['datasets']:
        if ds['canonical_name'] == name:
            return pd.read_csv(ds['access']['public_url'], nrows=nrows)
    raise ValueError(f"Dataset '{name}' not found")

# Elle collected from 55 YouTube influencer channels
# Study her column structure and metadata:
df = load_dataset("elle_morgan_ashley_absher_30_videos_ucvuw0xt38ho7qyumbgbzxqa")
print(f"Columns: {list(df.columns)}")
```

**Collection strategies to study:**
- `andrea_reddit_results_andrea_2025_03_13` - Reddit PRAW collection (871K posts)
- `peter_fox_msnbc_news` - News API collection (1.5M articles)
- `leighton_leighton_all_data` - Niche topic (golf) collection

**See:** `DATASETS_FOR_M4.md` for collection methodology details.

---

## Learning Goals
By the end of this lab, you will:
- Collect 100+ articles or posts on a topic of your choice
- Use keyword filtering effectively
- Apply date range filters
- Perform a basic data quality check
- Prepare data for analysis in Module 5

---

## Setup Instructions

### Step 1: Choose Your Topic
Before opening any code, decide on your research topic.

**Good Topic Examples:**
- Climate anxiety
- AI and job displacement
- Mental health on social media
- Sports psychology (specific athlete or event)
- Political polarization

**Topic Selection Criteria:**
- [ ] Is there enough online discussion about this? (Not too niche)
- [ ] Is it focused enough? (Not too broad)
- [ ] Does it interest you? (You'll be analyzing this data!)

**My chosen topic:** _______________________

### Step 2: Brainstorm Keywords
List 3-5 keywords or phrases for your topic:

1. _______________________
2. _______________________
3. _______________________
4. _______________________
5. _______________________

### Step 3: Open the Notebook
1. Open Google Colab
2. Upload `03_data_collection_boilerplate.ipynb`

---

## Part 1: Setup and Configuration (10 minutes)

### Cell 1: Install and Import

```python
# ============================================
# SETUP - Run this first
# ============================================
!pip install requests pandas -q

import requests
import pandas as pd
import time
from datetime import datetime, timedelta

print("Setup complete!")
```

### Cell 2: Configure Your Collection

```python
# ============================================
# CONFIGURATION - MODIFY THESE VARIABLES
# ============================================

# Your API key (provided by course)
API_KEY = "your-api-key-here"

# YOUR TOPIC - Change this!
TOPIC = "climate anxiety"

# Optional: Add keyword modifiers
# Use AND, OR, NOT for complex queries
KEYWORDS = '"climate change" AND (anxiety OR worry OR fear OR stress)'

# Date range
DATE_FROM = "2024-01-01"  # Start date (YYYY-MM-DD)
DATE_TO = "2024-12-31"    # End date (YYYY-MM-DD)

# How many articles to collect
MAX_ARTICLES = 100

# Language filter
LANGUAGE = "eng"  # "eng" for English

print(f"Collecting data on: {TOPIC}")
print(f"Keywords: {KEYWORDS}")
print(f"Date range: {DATE_FROM} to {DATE_TO}")
print(f"Target: {MAX_ARTICLES} articles")
```

---

## Part 2: Data Collection (20 minutes)

### Cell 3: News API Collection Function

```python
# ============================================
# NEWS COLLECTION FUNCTION
# ============================================

def collect_news_articles(keywords, api_key, date_from, date_to, max_results=100):
    """
    Collects news articles matching keywords.
    Returns a pandas DataFrame.
    """

    # API endpoint (example using Event Registry style)
    base_url = "https://newsapi.example.com/v2/articles"

    articles = []
    page = 1

    while len(articles) < max_results:
        print(f"Fetching page {page}...")

        params = {
            "q": keywords,
            "from": date_from,
            "to": date_to,
            "language": LANGUAGE,
            "pageSize": 50,
            "page": page,
            "apiKey": api_key
        }

        try:
            response = requests.get(base_url, params=params)
            data = response.json()

            if "articles" not in data or len(data["articles"]) == 0:
                print("No more articles found.")
                break

            for article in data["articles"]:
                articles.append({
                    "title": article.get("title", ""),
                    "description": article.get("description", ""),
                    "source": article.get("source", {}).get("name", ""),
                    "published_date": article.get("publishedAt", ""),
                    "url": article.get("url", ""),
                    "content": article.get("content", "")
                })

            page += 1
            time.sleep(0.5)  # Respect rate limits

        except Exception as e:
            print(f"Error: {e}")
            break

    # Convert to DataFrame
    df = pd.DataFrame(articles[:max_results])
    return df

# Note: This is a simplified example
# The actual notebook will have working API code
```

### Cell 4: Alternative - Use Provided Wrapper

```python
# ============================================
# SIMPLER VERSION - Using Course Wrapper
# ============================================

# If the full API is complex, use our simplified wrapper
from course_utils import collect_data

df = collect_data(
    topic=TOPIC,
    keywords=KEYWORDS,
    date_from=DATE_FROM,
    date_to=DATE_TO,
    max_results=MAX_ARTICLES,
    api_key=API_KEY
)

print(f"\nCollected {len(df)} articles!")
print(f"Columns: {list(df.columns)}")
```

### Cell 5: Run Collection

```python
# ============================================
# COLLECT YOUR DATA
# ============================================

print("Starting data collection...")
print("This may take 1-2 minutes...\n")

# Run collection (use the appropriate function from above)
df = collect_data(
    topic=TOPIC,
    keywords=KEYWORDS,
    date_from=DATE_FROM,
    date_to=DATE_TO,
    max_results=MAX_ARTICLES,
    api_key=API_KEY
)

print(f"\n{'='*50}")
print(f"COLLECTION COMPLETE!")
print(f"{'='*50}")
print(f"Total articles collected: {len(df)}")
```

---

## Part 3: Data Inspection (15 minutes)

### Cell 6: First Look at Your Data

```python
# ============================================
# INSPECT YOUR DATA
# ============================================

print("First 5 rows:")
print(df.head())

print("\n" + "="*50)
print("Data shape:", df.shape)
print("\nColumn types:")
print(df.dtypes)

print("\n" + "="*50)
print("Sample titles:")
for i, title in enumerate(df['title'].head(10)):
    print(f"{i+1}. {title[:80]}...")
```

### Cell 7: Quality Check

```python
# ============================================
# DATA QUALITY CHECK
# ============================================

print("DATA QUALITY REPORT")
print("="*50)

# Check for missing values
print("\n1. MISSING VALUES:")
print(df.isnull().sum())

# Check for duplicates
print(f"\n2. DUPLICATES:")
duplicates = df.duplicated(subset=['title']).sum()
print(f"Duplicate titles: {duplicates}")

# Check date range
print(f"\n3. DATE RANGE:")
df['published_date'] = pd.to_datetime(df['published_date'])
print(f"Earliest: {df['published_date'].min()}")
print(f"Latest: {df['published_date'].max()}")

# Check sources
print(f"\n4. TOP SOURCES:")
print(df['source'].value_counts().head(10))
```

### Cell 8: Relevance Check

```python
# ============================================
# RELEVANCE CHECK - READ SAMPLES
# ============================================

print("RANDOM SAMPLE FOR RELEVANCE CHECK")
print("="*50)
print("\nRead these 10 titles. Are they relevant to your topic?\n")

sample = df.sample(10, random_state=42)
for i, (idx, row) in enumerate(sample.iterrows()):
    print(f"{i+1}. {row['title']}")
    print(f"   Source: {row['source']}")
    print()

print("\nRELEVANCE ASSESSMENT:")
print("How many of these 10 are clearly relevant to your topic?")
print("_____ / 10")
print("\nIf less than 7/10, consider refining your keywords.")
```

---

## Part 4: Save and Prepare (10 minutes)

### Cell 9: Clean Data

```python
# ============================================
# BASIC CLEANING
# ============================================

# Remove duplicates
df_clean = df.drop_duplicates(subset=['title'])
print(f"Removed {len(df) - len(df_clean)} duplicates")

# Remove rows with missing titles
df_clean = df_clean.dropna(subset=['title'])
print(f"Rows after cleaning: {len(df_clean)}")

# Create a text column for analysis (combine title + description)
df_clean['full_text'] = df_clean['title'] + " " + df_clean['description'].fillna('')
print("\nCreated 'full_text' column for analysis")
```

### Cell 10: Save Your Dataset

```python
# ============================================
# SAVE YOUR DATA
# ============================================

# Create filename with your topic
filename = f"data_{TOPIC.replace(' ', '_')}_collected.csv"

df_clean.to_csv(filename, index=False)
print(f"Data saved to: {filename}")

# Download (in Colab)
from google.colab import files
files.download(filename)

print("\nThis data is ready for:")
print("- Module 3: AI rating")
print("- Module 5: Embedding generation")
print("- Your capstone project!")
```

---

## Part 5: Documentation (5 minutes)

### Complete Your Collection Log

Fill out this information for your Methods section:

**Data Collection Log:**

| Field | Your Value |
|-------|------------|
| API Used | |
| Topic/Keywords | |
| Date Range | |
| Language Filter | |
| Total Results Requested | |
| Total Results Received | |
| After Removing Duplicates | |
| Collection Date | |
| Relevance Check (X/10) | |

---

## Submission Checklist

### Required Deliverables:

1. **Screenshot:** First 5 rows of your collected data

2. **Collection Log:** Completed table above

3. **Relevance Assessment:**
   - How many of your 10 random samples were relevant? ___/10
   - If low, what keyword changes would you make?

4. **Saved CSV file:** Upload to course platform

---

## Troubleshooting

**"No results returned"**
- Keywords might be too specific
- Try removing quotes or using broader terms
- Check date range—is there coverage in that period?

**"Too many irrelevant results"**
- Add more specific keywords
- Use AND to require multiple terms
- Try adding NOT to exclude irrelevant topics

**"Rate limit error"**
- Add longer sleep delays: `time.sleep(2)`
- Reduce max_results for testing

**"API key error"**
- Check for typos
- Ensure no extra spaces
- Verify key hasn't expired

---

## Challenge Extension (Optional)

1. **Compare sources:** Collect from two different source types (e.g., news vs. Reddit) on the same topic. How do they differ?

2. **Time series:** Collect data across multiple months. Does coverage change over time?

3. **Multi-language:** If you speak another language, collect data in both and compare sentiment/tone.
