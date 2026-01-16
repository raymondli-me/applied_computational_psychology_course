# Module 4 Flashcards: Getting Real Data (APIs)

**Total Cards:** 21
**Format:** Anki-compatible (Front/Back)

---

## Definitions (5 cards)

### Card 1
**Front:** What is an API?
**Back:** Application Programming Interface - a structured, official way to request data from a service. Like placing an order at a restaurant - you make a request, they return data in a consistent format.
**Tags:** M4, definition, api

### Card 2
**Front:** What is web scraping?
**Back:** Extracting data directly from web pages by parsing HTML. Often unauthorized, unreliable, breaks when sites change. APIs are preferred when available.
**Tags:** M4, definition, collection

### Card 3
**Front:** What is a rate limit?
**Back:** Restriction on how many requests you can make per time period. Example: 60 requests/minute. Exceeding it gets you temporarily blocked or banned.
**Tags:** M4, definition, api

### Card 4
**Front:** What is pagination?
**Back:** Getting results in chunks (pages) rather than all at once. Most APIs return 50-100 items per request; you must loop through pages to get everything.
**Tags:** M4, definition, api

### Card 5
**Front:** What is an API key?
**Back:** A unique identifier that authenticates your requests. Like an ID card for your app. Keep it secret - leaked keys can be abused and you get blamed.
**Tags:** M4, definition, api

---

## Concepts (7 cards)

### Card 6
**Front:** Why use APIs instead of web scraping?
**Back:** APIs are: 1) Authorized (terms-compliant), 2) Reliable (consistent format), 3) Ethical, 4) Efficient. Scraping is unauthorized, breaks when sites change, and can get you banned.
**Tags:** M4, concept, ethics

### Card 7
**Front:** Why might "anxiety" return irrelevant results?
**Back:** Too broad - multiple meanings: stock market anxiety, sports anxiety, movie titles. Need specificity: "anxiety disorder" + "mental health" + "depression" with AND operators.
**Tags:** M4, concept, keywords

### Card 8
**Front:** What is keyword relevance?
**Back:** Proportion of collected items that match your actual research topic. If only 3/10 articles are relevant, your keywords are too broad. Test with small samples first.
**Tags:** M4, concept, quality

### Card 9
**Front:** What should you document about data collection?
**Back:** 1) API/source, 2) Keywords/query, 3) Date range, 4) Filters applied, 5) Total collected, 6) When collected, 7) Cleaning steps. Enables reproducibility.
**Tags:** M4, concept, documentation

### Card 10
**Front:** Why inspect data before analysis?
**Back:** Garbage in, garbage out. Without inspection, you might analyze: irrelevant content, duplicates that skew results, or broken data. 5 minutes of inspection saves hours.
**Tags:** M4, concept, quality

### Card 11
**Front:** What's the difference between AND and OR in queries?
**Back:** AND = requires both terms (narrows results). OR = either term (expands results). "AI AND jobs" finds articles about AI employment. "AI OR jobs" finds articles about either topic.
**Tags:** M4, concept, keywords

### Card 12
**Front:** When should you use quotes in search queries?
**Back:** For exact phrases. "mental health" finds that exact phrase. Without quotes, you get articles mentioning "mental" OR "health" separately. Quotes increase precision.
**Tags:** M4, concept, keywords

---

## Code Patterns (4 cards)

### Card 13
**Front:** How to handle rate limits in code:
**Back:**
```python
import time
for item in items:
    result = api_call(item)
    time.sleep(1)  # Wait 1 second between calls
```
**Tags:** M4, code, api

### Card 14
**Front:** How to remove duplicates from collected data:
**Back:**
```python
df = df.drop_duplicates(subset=['post_id'])
# Or for text duplicates:
df = df.drop_duplicates(subset=['title', 'source'])
```
**Tags:** M4, code, cleaning

### Card 15
**Front:** How to check relevance of collected data:
**Back:**
```python
# Sample 10 random items
sample = df.sample(10)
for _, row in sample.iterrows():
    print(row['title'][:100])
# Manually count relevant items
```
**Tags:** M4, code, quality

### Card 16
**Front:** How to filter data by date:
**Back:**
```python
df['date'] = pd.to_datetime(df['published_at'])
df_recent = df[df['date'] > '2023-01-01']
```
**Tags:** M4, code, cleaning

---

## Interpretation (3 cards)

### Card 17
**Front:** You collected 5,000 articles but only 500 unique. What happened?
**Back:** High duplicate rate. Possible causes: 1) Same article from multiple sources, 2) API returning same results multiple pages, 3) Syndicated content. Always deduplicate before analysis.
**Tags:** M4, interpretation, quality

### Card 18
**Front:** Relevance check: 3/10 articles about your topic. What to do?
**Back:** Revise keywords. Too broad. Add more specific terms, use AND to require multiple concepts, or exclude irrelevant sources. Re-collect with better query before wasting time on analysis.
**Tags:** M4, interpretation, keywords

### Card 19
**Front:** API returns "429 Too Many Requests". What happened?
**Back:** Hit rate limit. Solution: Add time.sleep() delays between requests, reduce request frequency, or wait until limit resets (usually 1-15 minutes). Don't hammer the API.
**Tags:** M4, interpretation, troubleshooting

---

## Common Mistakes (2 cards)

### Card 20
**Front:** What's wrong with sharing your API key publicly?
**Back:** Anyone can use your key, potentially: 1) Exceeding your quota (costing you money), 2) Getting you banned, 3) Doing things that violate terms of service under your identity.
**Tags:** M4, mistake, security

### Card 21
**Front:** What's wrong with not checking date range?
**Back:** You might have data from 10 years ago when you wanted recent content, or data clustered in one week with gaps. Always verify: `df['date'].min()` and `df['date'].max()`.
**Tags:** M4, mistake, quality

---

*Module 4 Flashcards | Applied Psychological Data Science*
