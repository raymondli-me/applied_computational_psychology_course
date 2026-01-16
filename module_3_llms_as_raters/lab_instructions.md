# Module 3 Lab: Building an AI Rater

## Lab Overview
**Duration:** 90 minutes
**Tools Required:** Google Colab, OpenAI API key
**Dataset:** Yashita's YouTube Data or Kaitlyn's Mental Health Data (from course dataset bank)

---

## Learning Goals
By the end of this lab, you will:
- Write an effective rating prompt for a psychological construct
- Use the OpenAI API to rate text at scale
- Calculate human-AI agreement (correlation)
- Iterate on your prompt to improve agreement

---

## Setup Instructions

### Step 1: Open the Course Notebook
1. Go to the course repository on GitHub
2. Click the "Open in Colab" badge
3. Make sure you've run the setup cell to enable `load_dataset()`

### Step 2: Get Your API Key
1. The course may provide a shared API key (check announcements)
2. OR create your own at [platform.openai.com](https://platform.openai.com)
3. Keep your API key secret - never commit it to GitHub!

### Step 3: Load the Dataset

```python
# Load Yashita's YouTube data - small, good for testing prompts
df = load_dataset("yashita_yashita_data")
print(f"Loaded {len(df):,} rows")
print(f"Columns: {list(df.columns)}")

# We'll rate video descriptions for OPTIMISM
# Take a sample for practice
df_sample = df.head(50).copy()
print(f"\nUsing {len(df_sample)} rows for practice")
df_sample[['video_title', 'description']].head()
```

**Alternative for validation (with human ratings):**
```python
# Kaitlyn's data has human ground truth ratings
df = load_dataset("kaitlyn_merged_data_overview_kaitlyn_master", nrows=100)
```

---

## Part 1: Human Rating Practice (15 minutes)

Before asking AI to rate, YOU will rate some items first.

### Task: Rate 10 Video Descriptions for OPTIMISM

**Definition:** Optimism refers to the expression of positive expectations, hope, or favorable outlooks in the text.

**Scale:**
- 1 = Very pessimistic (negative, hopeless)
- 4 = Neutral (factual, neither positive nor negative)
- 7 = Very optimistic (hopeful, positive, encouraging)

```python
# View 10 items to rate
for i, row in df_sample.head(10).iterrows():
    print(f"\n--- Item {i+1} ---")
    print(f"Title: {row['video_title'][:80]}...")
    desc = str(row['description'])[:200] if pd.notna(row['description']) else "(no description)"
    print(f"Description: {desc}...")
    print()
```

**Your Task:** Rate each of the 10 items. Record your ratings:
```python
# Enter YOUR ratings for items 0-9
my_ratings = {
    0: _,  # Your rating for item 0
    1: _,
    2: _,
    3: _,
    4: _,
    5: _,
    6: _,
    7: _,
    8: _,
    9: _,
}
```

---

## Part 2: Setting Up the AI Rater (10 minutes)

### Install OpenAI and set up client

```python
!pip install openai -q

import openai
import time

# Enter your API key (keep this secret!)
API_KEY = "your-api-key-here"  # Replace with your actual key
client = openai.OpenAI(api_key=API_KEY)

# Test connection
try:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": "Say 'connected' and nothing else"}],
        max_tokens=10
    )
    print("API Connected:", response.choices[0].message.content)
except Exception as e:
    print("Connection failed:", e)
```

### Define Your Rating Prompt

```python
def create_prompt(text):
    """
    Creates a rating prompt for a piece of text.
    MODIFY THIS to improve your results!
    """
    prompt = f"""You are a research assistant helping code text for psychological research.

TASK: Rate the following text on OPTIMISM.

DEFINITION: Optimism refers to the expression of positive expectations, hope, or favorable outlooks.

SCALE:
1 = Very pessimistic (negative, hopeless, discouraging)
4 = Neutral (factual, neither positive nor negative)
7 = Very optimistic (hopeful, positive, encouraging)

TEXT TO RATE:
"{text}"

Provide ONLY a single number (1-7) as your response."""

    return prompt

# Test your prompt
test_text = "This video will change your life! Amazing results guaranteed!"
print(create_prompt(test_text))
```

---

## Part 3: Running the AI Rater (20 minutes)

### Rating Function

```python
def get_ai_rating(text, max_retries=3):
    """Get AI rating for a single text. Returns int 1-7 or None."""
    if pd.isna(text) or str(text).strip() == "":
        return None

    prompt = create_prompt(str(text)[:500])  # Limit text length

    for attempt in range(max_retries):
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
                temperature=0,  # CRITICAL: 0 for consistency
                max_tokens=5
            )
            rating = int(response.choices[0].message.content.strip())
            if 1 <= rating <= 7:
                return rating
        except Exception as e:
            time.sleep(1)

    return None
```

### Rate All Items

```python
print("Rating items with AI... (this takes a few minutes)")

ai_ratings = []
for i, row in df_sample.iterrows():
    text = row.get('description', row.get('video_title', ''))
    rating = get_ai_rating(text)
    ai_ratings.append(rating)

    if (i + 1) % 10 == 0:
        print(f"Rated {i + 1}/{len(df_sample)}")

df_sample['ai_rating'] = ai_ratings
print(f"\nDone! Got {df_sample['ai_rating'].notna().sum()} valid ratings")
```

---

## Part 4: Calculate Agreement (15 minutes)

### Add Your Human Ratings

```python
# Add your human ratings for the first 10 items
human_ratings = [None] * len(df_sample)

# Fill in your ratings from Part 1
my_ratings = {
    0: 5,  # Replace with your actual ratings
    1: 3,
    2: 6,
    # ... etc
}

for idx, rating in my_ratings.items():
    human_ratings[idx] = rating

df_sample['human_rating'] = human_ratings
```

### Calculate Correlation

```python
from scipy import stats

# Get rows where both human and AI rated
df_valid = df_sample.dropna(subset=['ai_rating', 'human_rating'])

if len(df_valid) >= 3:
    correlation, p_value = stats.pearsonr(
        df_valid['human_rating'],
        df_valid['ai_rating']
    )

    print("=" * 50)
    print("HUMAN-AI AGREEMENT RESULTS")
    print("=" * 50)
    print(f"Correlation (r): {correlation:.3f}")
    print(f"P-value: {p_value:.4f}")
    print(f"N items compared: {len(df_valid)}")

    if correlation > 0.80:
        print("\n✓ EXCELLENT agreement!")
    elif correlation > 0.60:
        print("\n✓ GOOD agreement")
    elif correlation > 0.40:
        print("\n~ MODERATE - consider refining prompt")
    else:
        print("\n✗ LOW - revise prompt significantly")
else:
    print("Need at least 3 items with both ratings to calculate correlation")
```

### Examine Disagreements

```python
# Where did human and AI disagree most?
df_valid['difference'] = abs(df_valid['human_rating'] - df_valid['ai_rating'])

print("\nBIGGEST DISAGREEMENTS:")
print("=" * 60)
for _, row in df_valid.nlargest(3, 'difference').iterrows():
    text = str(row.get('description', row.get('video_title', '')))[:60]
    print(f"\nText: {text}...")
    print(f"Human: {row['human_rating']} | AI: {row['ai_rating']}")
```

---

## Part 5: Iterate & Improve (15 minutes)

Based on disagreements, improve your prompt:

### Common Improvements

1. **Add examples:**
```python
prompt = """...
EXAMPLES:
- "Everything is terrible and will only get worse" → 1
- "The meeting is scheduled for Tuesday" → 4
- "Exciting breakthrough offers new hope!" → 7
..."""
```

2. **Clarify edge cases:**
```python
prompt = """...
NOTE: Promotional/clickbait language ("AMAZING!") should be rated
based on actual content, not just enthusiasm.
..."""
```

3. **Be more specific:**
```python
prompt = """...
Rate based on:
- Positive future expectations = higher scores
- Negative predictions or warnings = lower scores
- Neutral facts without valence = middle scores
..."""
```

### Re-run and Compare

After modifying `create_prompt()`, run the rating again and compare correlations.

---

## Submission Checklist

### Required Deliverables:

1. **Your Final Prompt** (copy the full text)

2. **Agreement Statistics:**
   - Correlation (r): ___________
   - P-value: ___________
   - N items: ___________

3. **Disagreement Analysis** (2-3 sentences):
   - Describe one major disagreement
   - Why did human and AI differ?
   - How would you fix the prompt?

4. **Screenshot:** Your correlation output

---

## Troubleshooting

**"AuthenticationError"**
- Check your API key - no extra spaces
- Make sure it starts with "sk-"

**"RateLimitError"**
- Add `time.sleep(1)` between requests
- Or wait a few minutes and retry

**"AI returns text instead of number"**
- Add "Respond with ONLY a single digit" to your prompt
- Make sure temperature=0

**"Very low correlation"**
- Check: Are YOU consistent? Re-rate 5 items
- Check: Is your definition clear?
- Try adding examples to the prompt

---

## Key Takeaways

Before moving to Module 4:

1. **Prompt = Survey Question** - same design principles apply
2. **Temperature = 0** for reproducible ratings
3. **Always validate** against human judgment
4. **Iterate** - first prompt is rarely best
