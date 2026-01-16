# Module 3 Lab: Building an AI Rater

## Lab Overview
**Duration:** 60 minutes
**Tools Required:** Google Colab, OpenAI API access (provided)
**Dataset:** Choose from course dataset bank (see below)
**Notebook:** `02_llm_rating_boilerplate.ipynb`

---

## Dataset Options for This Lab

### Recommended: Kaitlyn's Mental Health Data (with human ground truth)
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

# Kaitlyn's Mental Health Data - 809K comments with human ratings
# Sample for practice:
df = load_dataset("kaitlyn_merged_data_overview_kaitlyn_master", nrows=100)
print(f"Loaded {len(df):,} rows")
```

*Kaitlyn's 6-rater team achieved κ > 0.80 reliability across 23 mental health conditions - use as ground truth for your LLM prompts.*

**Alternative for small-scale testing:**
```python
# Peter's GPT-analyzed news data
df = load_dataset("peter_fox_msnbc_100video_gpt_data_to_analyze_mar9_2025", nrows=50)
```

**See:** `DATASETS_FOR_M3.md` for all options.

---

## Learning Goals
By the end of this lab, you will:
- Write an effective rating prompt for a psychological construct
- Use the OpenAI API to rate text at scale
- Calculate human-AI agreement (correlation)
- Iterate on your prompt to improve agreement

---

## Setup Instructions

### Step 1: Get Your API Key
1. The course provides a shared API key (check course announcements)
2. OR create your own at [platform.openai.com](https://platform.openai.com)
3. Keep your API key secret - never share it publicly

### Step 2: Open the Notebook
1. Open Google Colab
2. Upload `02_llm_rating_boilerplate.ipynb`
3. Upload `news_headlines_50.csv`

---

## Part 1: Human Rating (15 minutes)

Before we ask the AI to rate anything, YOU will rate the headlines.

### Task: Rate Headlines for OPTIMISM

**Definition:** Optimism refers to the expression of positive expectations, hope, or favorable outlooks about the future in the headline.

**Scale:**
- 1 = Very pessimistic (doom, disaster, negative outlook)
- 4 = Neutral (factual, neither optimistic nor pessimistic)
- 7 = Very optimistic (hopeful, positive, encouraging outlook)

### Your Rating Task

Open `news_headlines_50.csv` and rate ALL 50 headlines. Record your ratings in a new column called `human_rating`.

**Sample headlines and example ratings:**
| Headline | Rating | Reasoning |
|----------|--------|-----------|
| "Economy Expected to Grow Despite Challenges" | 5 | Slightly optimistic - acknowledges challenges but expects growth |
| "Scientists Warn of Irreversible Climate Damage" | 2 | Pessimistic - warning, irreversible, damage |
| "Local School Wins National Science Competition" | 6 | Optimistic - positive achievement, success |

**Tips:**
- Work quickly - trust your gut reaction
- Don't overthink - first impression matters
- Be consistent - would you rate similar headlines similarly?

---

## Part 2: Setting Up the AI Rater (10 minutes)

### Cell 1: Setup
```python
# ============================================
# SETUP - Run this cell first
# ============================================
!pip install openai pandas -q

import openai
import pandas as pd
import time

# Enter your API key
API_KEY = "your-api-key-here"  # Replace with actual key
client = openai.OpenAI(api_key=API_KEY)

# Load data
df = pd.read_csv('news_headlines_50.csv')
print(f"Loaded {len(df)} headlines")
print(df.head())
```

### Cell 2: Define Your Rating Prompt

```python
# ============================================
# YOUR RATING PROMPT - MODIFY THIS
# ============================================

def create_prompt(headline):
    """
    Creates a rating prompt for a single headline.
    MODIFY the prompt below to rate for OPTIMISM.
    """

    prompt = f"""You are a research assistant helping code news headlines for psychological research.

TASK: Rate the following headline on OPTIMISM.

DEFINITION: Optimism refers to the expression of positive expectations, hope, or favorable outlooks about the future in the headline.

SCALE:
1 = Very pessimistic (doom, disaster, negative outlook)
4 = Neutral (factual, neither optimistic nor pessimistic)
7 = Very optimistic (hopeful, positive, encouraging outlook)

HEADLINE TO RATE:
"{headline}"

Provide ONLY a single number (1-7) as your response."""

    return prompt

# Test your prompt
test_headline = "Scientists Discover Breakthrough Treatment for Cancer"
print("Testing prompt with:", test_headline)
print("\n" + create_prompt(test_headline))
```

---

## Part 3: Running the AI Rater (15 minutes)

### Cell 3: Rate Function

```python
# ============================================
# AI RATING FUNCTION
# ============================================

def get_ai_rating(headline, max_retries=3):
    """
    Gets an AI rating for a single headline.
    Returns an integer 1-7 or None if failed.
    """
    prompt = create_prompt(headline)

    for attempt in range(max_retries):
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",  # Fast and cheap
                messages=[{"role": "user", "content": prompt}],
                temperature=0,  # CRITICAL: Set to 0 for consistency
                max_tokens=5
            )

            # Extract the number
            rating_text = response.choices[0].message.content.strip()
            rating = int(rating_text)

            # Validate range
            if 1 <= rating <= 7:
                return rating
            else:
                print(f"Warning: Rating {rating} out of range for: {headline[:50]}...")
                return None

        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            time.sleep(1)

    return None
```

### Cell 4: Rate All Headlines

```python
# ============================================
# RATE ALL HEADLINES
# ============================================

print("Starting AI rating... (this may take a few minutes)")

ai_ratings = []
for i, row in df.iterrows():
    headline = row['headline']
    rating = get_ai_rating(headline)
    ai_ratings.append(rating)

    # Progress update every 10 items
    if (i + 1) % 10 == 0:
        print(f"Rated {i + 1}/{len(df)} headlines")

# Add to dataframe
df['ai_rating'] = ai_ratings

# Show results
print("\nSample of ratings:")
print(df[['headline', 'ai_rating']].head(10))

# Save results
df.to_csv('headlines_with_ai_ratings.csv', index=False)
print("\nResults saved to headlines_with_ai_ratings.csv")
```

---

## Part 4: Calculate Agreement (10 minutes)

### Cell 5: Add Your Human Ratings

```python
# ============================================
# ADD YOUR HUMAN RATINGS
# ============================================

# Option 1: Enter manually (if you rated in a separate sheet)
# Replace these with YOUR actual ratings
human_ratings = [
    5, 2, 6, 4, 3, 7, 2, 5, 4, 6,  # Headlines 1-10
    # ... add all 50 ratings
]

# Option 2: Load from file
# df_human = pd.read_csv('your_human_ratings.csv')
# human_ratings = df_human['human_rating'].tolist()

df['human_rating'] = human_ratings
```

### Cell 6: Calculate Correlation

```python
# ============================================
# CALCULATE HUMAN-AI AGREEMENT
# ============================================
from scipy import stats

# Remove any rows where AI failed to rate
df_valid = df.dropna(subset=['ai_rating', 'human_rating'])

# Calculate Pearson correlation
correlation, p_value = stats.pearsonr(
    df_valid['human_rating'],
    df_valid['ai_rating']
)

print("=" * 50)
print("HUMAN-AI AGREEMENT RESULTS")
print("=" * 50)
print(f"Correlation (r): {correlation:.3f}")
print(f"P-value: {p_value:.4f}")
print(f"Number of valid ratings: {len(df_valid)}")

# Interpretation
if correlation > 0.80:
    print("\nInterpretation: EXCELLENT agreement - AI matches your judgment closely")
elif correlation > 0.60:
    print("\nInterpretation: GOOD agreement - AI captures the construct reasonably")
elif correlation > 0.40:
    print("\nInterpretation: MODERATE agreement - Consider refining your prompt")
else:
    print("\nInterpretation: POOR agreement - Major prompt revision needed")
```

### Cell 7: Examine Disagreements

```python
# ============================================
# ANALYZE DISAGREEMENTS
# ============================================

# Calculate difference
df_valid['difference'] = abs(df_valid['human_rating'] - df_valid['ai_rating'])

# Find biggest disagreements
disagreements = df_valid.nlargest(5, 'difference')[
    ['headline', 'human_rating', 'ai_rating', 'difference']
]

print("BIGGEST DISAGREEMENTS (Human vs. AI):")
print("=" * 60)
for _, row in disagreements.iterrows():
    print(f"\nHeadline: {row['headline'][:60]}...")
    print(f"Human: {row['human_rating']} | AI: {row['ai_rating']} | Diff: {row['difference']}")
```

---

## Part 5: Iterate & Improve (10 minutes)

Based on the disagreements, consider:

1. **Is your definition clear?**
   - Did the AI interpret "optimism" differently?

2. **Are your anchors specific enough?**
   - Maybe the midpoint needs more detail?

3. **Is your own rating consistent?**
   - Would you rate the disagreement items the same way again?

### Task: Revise Your Prompt

Go back to Cell 2 and modify your prompt. Then re-run the rating.

**Common Improvements:**
- Add examples: "A headline like 'Cure Found for Disease' would be a 7"
- Clarify edge cases: "Headlines about neutral events should be 4"
- Be more specific about what counts

---

## Submission Checklist

### Required Deliverables:

1. **Your Final Prompt** (copy-paste the full text)

2. **Correlation Coefficient:**
   - Your r value: ___________
   - P-value: ___________
   - Interpretation: ___________

3. **Disagreement Analysis** (2-3 sentences):
   - Describe one major disagreement
   - Explain why you think human and AI differed
   - How might you revise the prompt to address this?

4. **Screenshot:** Your correlation output

---

## Troubleshooting

**"Authentication Error"**
- Double-check your API key
- Make sure there are no extra spaces

**"Rate limit exceeded"**
- The free tier has limits
- Add `time.sleep(1)` between requests

**"AI returns non-number responses"**
- Add "Provide ONLY a number" to your prompt
- Check that temperature is set to 0

**"Very low correlation"**
- Don't panic - this is a learning opportunity
- Check: Are YOU consistent? Re-rate 10 items and see if you agree with yourself

---

## Challenge Extension (Optional)

1. **Try a different construct:**
   - Rate for "FEAR" instead of optimism
   - How does agreement compare?

2. **Compare models:**
   - Run with gpt-4o-mini vs. gpt-4o
   - Is the more expensive model more accurate?

3. **Few-shot learning:**
   - Add 3 example ratings to your prompt
   - Does agreement improve?
