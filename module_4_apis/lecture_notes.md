# Module 4: Lecture Script
## "The Data Pipeline: How to Download the Internet's Opinion"

**Total Runtime:** ~38 minutes
**Video Production Ready:** Yes

---

### INTRO [0:00-2:00]
*[INSTRUCTOR NOTE: The scale numbers from Elle/Andrea/Peter establish credibility and set expectations]*

**[SLIDE: Course Dataset Contributors - Elle, Andrea, Peter]**

*"Elle collected data from 55 YouTube channels—59 datasets total. Andrea scraped 871,000 Reddit posts about wedding conflicts. Peter downloaded 1.5 million news articles from Fox and MSNBC."*

*"How did they do it? APIs. Today, you learn the exact methods they used."*

---

### SECTION 1: WHAT IS AN API? [2:00-9:00]
*[INSTRUCTOR NOTE: The restaurant analogy is key—make sure students can explain it back]*

**[SLIDE: Restaurant analogy]**

*"Let me give you the restaurant analogy."*

*"When you go to a restaurant, you don't walk into the kitchen and grab food off the stove. You sit at a table, look at a menu, and tell the waiter what you want. The waiter takes your order to the kitchen and brings back your meal."*

**[CLICK: Label the diagram]**

*"An API is the waiter. The kitchen is the database. The menu is the documentation. And your order is the request."*

*"API stands for Application Programming Interface. It's a structured way for your code to ask another system for data."*

**[SLIDE: Code example]**

```python
# Your "order" to the news API
response = api.get_articles(
    topic="climate anxiety",
    language="english",
    date_from="2024-01-01"
)
```

*"You specify what you want—topic, language, date range—and the API brings it back in a structured format."*

**[SLIDE: JSON response example]**

*"What comes back looks like this—JSON. It's basically a dictionary: keys and values. Headline, source, date, text. Structured. Ready for analysis."*

---

### SECTION 2: THE KEYWORD PROBLEM [9:00-17:00]
*[INSTRUCTOR NOTE: This is where most students fail—emphasize keyword selection as a SKILL]*

**[SLIDE: Search bar]**

*"The most important decision in data collection isn't the API you use. It's the KEYWORDS you search for."*

**[SLIDE: Bad keyword example]**

*"Imagine you're studying 'anxiety.' You search for 'anxiety.' What do you get?"*

- *Articles about the movie 'Anxiety'*
- *Stock market anxiety*
- *"I have anxiety about my pizza delivery"*
- *Clinical anxiety research*
- *Performance anxiety in sports*

*"Your data is now a mess. Half of it isn't relevant to your research question."*

**[SLIDE: Good keyword strategy]**

*"Better approach: Be specific but not too narrow."*

| Too Broad | Better | Too Narrow |
|-----------|--------|------------|
| anxiety | mental health anxiety | generalized anxiety disorder DSM-5 |
| depression | depression treatment | treatment-resistant depression SSRIs |
| politics | election 2024 | senate race wisconsin district 3 |

*"You want a Goldilocks zone—specific enough to be relevant, broad enough to have data."*

**[SLIDE: Keyword combinations]**

*"Pro tip: Use AND/OR logic."*

```python
# Combine keywords
topic = '"climate change" AND (anxiety OR worry OR fear)'
```

*"This gets articles that mention climate change AND at least one of those emotion words. Much more targeted."*

---

### SECTION 3: FILTERS—DATE, SOURCE, LANGUAGE [17:00-23:00]
*[PAUSE: Check understanding of keyword strategy before introducing filters]*

**[SLIDE: Filter options]**

*"Beyond keywords, APIs let you filter data."*

**Date Filtering**

*"Why filter by date? Two reasons."*

1. *"Recency: You might only want recent coverage"*
2. *"Event-based: You want coverage DURING a specific event"*

*"Studying how news covered COVID vaccines? Filter to 2021. Studying Draymond Green suspensions? Filter to the week of the incident."*

**Source Filtering**

*"Some APIs let you filter by source. Want only major news outlets? Filter. Want only left-leaning or right-leaning sources? Filter."*

*"But be careful—filtering sources can introduce bias. Document your choices."*

**Language Filtering**

*"If you're studying English-language discourse, filter for English. Otherwise you'll get results in languages you can't analyze."*

---

### SECTION 4: RATE LIMITS AND QUOTAS [23:00-28:00]
*[INSTRUCTOR NOTE: Students often skip this and get blocked—emphasize consequences]*

**[SLIDE: Traffic light]**

*"APIs aren't unlimited. They have RATE LIMITS."*

*"A rate limit says: You can make X requests per Y time period."*

*"Example: 100 requests per minute. That means if you try to make 150 requests in one minute, the API will block you after 100."*

**[SLIDE: Code with delay]**

*"Solution: Add delays between requests."*

```python
import time

for article in articles:
    data = api.get(article)
    time.sleep(0.5)  # Wait half a second between requests
```

*"It's slower, but you won't get blocked."*

**[SLIDE: Quotas]**

*"Some APIs have QUOTAS—a total limit per day or month."*

*"YouTube API: 10,000 units per day. Some operations cost 1 unit, others cost 100. Plan accordingly."*

*"Free tiers are generous enough for coursework. If you need more, there are paid options—but let's start free."*

---

### SECTION 5: DATA QUALITY CHECK [28:00-33:00]
*[INSTRUCTOR NOTE: "Garbage in, garbage out" is the key message—make it memorable]*

**[SLIDE: Garbage in, garbage out]**

*"You've collected 1,000 articles. Now what?"*

*"DO NOT immediately run analysis. First, INSPECT YOUR DATA."*

**[SLIDE: Quality check checklist]**

*"Quality check checklist:"*

1. *"Are results relevant? Read 20 random samples. How many are on-topic?"*
2. *"Are there duplicates? Same article from different sources?"*
3. *"Is the date range correct? Any articles from outside your window?"*
4. *"Are there obvious errors? Missing text, garbled characters?"*

*"If more than 10-20% of your data is irrelevant, go back and refine your keywords."*

**[SLIDE: Document everything]**

*"Finally: DOCUMENT your collection process."*

*"Future you (and your readers) need to know:"*
- *What API did you use?*
- *What keywords?*
- *What date range?*
- *What filters?*
- *How many results?*

*"This goes in your Methods section. Reproducibility matters."*

---

### WRAP-UP [33:00-35:00]

**[SLIDE: Today's Takeaways]**

*"Key points:"*

1. *"APIs are structured ways to request data—learn to use them"*
2. *"Keywords make or break your dataset—be specific but not too narrow"*
3. *"Use filters: date, source, language"*
4. *"Respect rate limits—add delays, don't spam servers"*
5. *"ALWAYS check data quality before analysis"*

*"In lab, you'll collect your own dataset. You'll choose a topic, write keywords, and download 100 articles. By the end, you'll have real data ready for the next phase: turning text into numbers with embeddings."*

*"Let's collect some data."*

---

### SECTION 6: LEARNING FROM COURSE CONTRIBUTORS [35:00-38:00]
*[LIVE CODING: Show how to explore contributor datasets—students follow along]*

**[LIVE DEMO: Exploring contributor datasets]**

```python
# See how Elle collected YouTube data
list_datasets(contributor="Elle")  # 59 datasets!

# Load Andrea's Reddit collection
df = load_dataset("andrea_reddit_results_andrea_2025_03_13")
print(f"Andrea collected {len(df):,} Reddit posts")

# Load Peter's news collection
df_news = load_dataset("peter_fox_msnbc_news")
print(f"Peter collected {len(df_news):,} news articles")
```

*"Each of these datasets has a story. Andrea targeted wedding-related subreddits with specific keywords. Peter used source filtering to compare Fox vs. MSNBC. Elle systematically worked through 55 YouTube channels. Study their approaches in DATASETS_FOR_M4.md before you design your own collection."*

---

### LECTURE MATERIALS CHECKLIST
- [ ] API analogy diagram
- [ ] Keyword examples from real course datasets (Andrea, Peter)
- [ ] JSON response example
- [ ] Rate limit explanation
- [ ] Data quality checklist slide
- [ ] DATASETS_FOR_M4.md reference card
