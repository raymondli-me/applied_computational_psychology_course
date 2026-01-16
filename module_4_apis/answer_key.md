# Module 4 Answer Key: Data Collection (APIs)
## INSTRUCTOR USE ONLY

**Assessment:** Module 4 Assessment
**Exemplar Collections:** Elle (YouTube), Andrea (Reddit), Peter (News)
**Total Points:** 100

---

## Part A: Concept Check (25 points)

### Question 1 (5 points)
**Question:** What is an API, and how does it differ from web scraping?

**Model Answer:**
> An API (Application Programming Interface) is a structured, official way to request data from a service—like placing an order at a restaurant. It's authorized, reliable, and returns data in a consistent format. Web scraping is extracting data directly from web pages, often without explicit permission. APIs are preferred because they're more reliable, ethical, and less likely to break when websites change.

**Rubric:**
| Score | Criteria |
|-------|----------|
| 5 | Defines API + distinguishes from scraping + mentions reliability/ethics |
| 3 | Correct distinction but incomplete |
| 1 | Vague understanding |
| 0 | Incorrect |

**Key Points:**
- API = structured, authorized, reliable
- Scraping = extracting from HTML, unofficial
- APIs preferred for reproducibility

---

### Question 2 (5 points)
**Question:** Why might "anxiety" return irrelevant results when studying mental health?

**Model Answer:**
> "Anxiety" is too broad and has multiple meanings beyond mental health: stock market anxiety, anxiety about sports outcomes, movie titles, etc. Without additional context or filtering, you'll get a mix of content that doesn't relate to psychological anxiety, making your dataset noisy and reducing validity.

**Rubric:**
| Score | Criteria |
|-------|----------|
| 5 | Multiple meanings identified + validity concern mentioned |
| 3 | Recognizes broad term but vague on consequences |
| 1 | Mentions "too broad" without specifics |
| 0 | Incorrect |

**Examples of "anxiety" false positives:**
- "Investor anxiety over Fed rates"
- "Pre-game anxiety"
- Movie: "Anxiety" (2024)
- "Separation anxiety" in pets

---

### Question 3 (5 points)
**Question:** What is a rate limit, and how should you handle it?

**Correct Answer:** B) A limit on requests per time period; add delays between requests

**Rubric:**
| Score | Criteria |
|-------|----------|
| 5 | Selects B |
| 0 | Any other answer |

**Instructor Note:** Common APIs and their rate limits:
- News API: 100/day (free tier)
- YouTube: 10,000 units/day
- Reddit: 60/minute

---

### Question 4 (5 points)
**Question:** Why inspect data BEFORE running analysis?

**Model Answer:**
> To ensure data quality and relevance. Without inspection, you might analyze irrelevant articles (garbage in, garbage out), miss duplicates that skew results, or not notice missing values. A quick quality check catches problems early when they're easier to fix.

**Rubric:**
| Score | Criteria |
|-------|----------|
| 5 | Mentions relevance check + quality issues + early detection |
| 3 | Some quality concerns but incomplete |
| 1 | Vague mention of "checking" |
| 0 | Incorrect |

---

### Question 5 (5 points)
**Question:** What should you document about data collection for Methods?

**Model Answer:**
> Document: (1) the API/source used, (2) exact keywords and search query, (3) date range, (4) any filters applied, (5) total number collected, (6) collection date, and (7) cleaning steps. This enables reproducibility.

**Rubric:**
| Score | Criteria |
|-------|----------|
| 5 | 5+ elements mentioned + reproducibility goal |
| 3 | 3-4 elements |
| 1 | 1-2 elements |
| 0 | Incorrect or no response |

---

## Part B: Keyword Design (25 points)

### Scenario 1: AI Jobs (10 points)

**Given keyword:** `AI`

**Problems (expected answers):**
1. "AI" alone returns general AI content, not job-related
2. "AI" catches false positives (company names, acronyms)
3. Too broad—millions of results, mostly irrelevant

**Improved Query:**
```
"artificial intelligence" AND (jobs OR employment OR workers OR unemployment OR "job loss" OR automation)
```

**Rubric:**
| Component | Points | Criteria |
|-----------|--------|----------|
| Problem 1 | 3 | Valid issue identified |
| Problem 2 | 3 | Valid issue identified |
| Improved query | 4 | Uses AND/OR, includes job-related terms |

**Acceptable Alternative Queries:**
- `AI AND "job loss"`
- `"artificial intelligence" AND unemployment`
- `AI AND (workers OR automation OR "jobs replaced")`

---

### Scenario 2: Teen Mental Health (10 points)

**Model Query:**
```
("social media" OR Instagram OR TikTok OR Snapchat) AND (teen OR adolescent OR youth) AND ("mental health" OR depression OR anxiety OR wellbeing)
```

**Model Filters:**
- Date range: 2020-01-01 to present
- Language: English
- Other: Exclude marketing/promotional sources

**Rubric:**
| Component | Points | Criteria |
|-----------|--------|----------|
| Query structure | 5 | Uses AND/OR, has platform + age + mental health terms |
| Filters | 5 | Reasonable date, language, other constraints |

---

### Best Practices (5 points)

**Expected Answers (any 3):**
1. Use quotes for exact phrases
2. Use AND/OR operators appropriately
3. Test with small sample first
4. Start broad, then narrow
5. Include synonyms
6. Exclude irrelevant terms with NOT

**Rubric:** 1-2 points per valid best practice

---

## Part C: Lab Results (50 points)

### Task 1: Collection Summary (15 points)

**Checklist:**
| Field | Points | Criteria |
|-------|--------|----------|
| Topic chosen | 2 | Clear research question |
| Keywords used | 3 | Specific, relevant |
| Date range | 2 | Reasonable for topic |
| API/Source | 2 | Identified correctly |
| Articles requested | 2 | Number stated |
| Articles received | 2 | Number stated |
| After dedup | 2 | Shows cleaning happened |

---

### Task 2: Data Preview (10 points)

**Screenshot Requirements:**
| Element | Points |
|---------|--------|
| First 5 rows visible | 3 |
| Column names visible | 2 |
| Total row count | 2 |
| Title + source columns | 3 |

---

### Task 3: Quality Assessment (15 points)

**Relevance Check (5 points):**
- 10/10: 5 points
- 7-9/10: 4 points
- 4-6/10: 3 points + reasonable improvement suggestion
- <4/10: 2 points + must suggest improvement

**Duplicate Check (5 points):**
- States number removed: 5 points
- Shows deduplication happened

**Date Range Check (5 points):**
- Dates provided: 3 points
- Within expected range: 2 points

---

### Task 4: Reflection (10 points)

**Rubric:**
| Component | Points | Criteria |
|-----------|--------|----------|
| Keyword challenges | 3 | Specific challenge identified |
| Surprises | 3 | Concrete example |
| Refinement ideas | 4 | Actionable improvements |

**Good Reflections Include:**
- "I found that [term] also matched [unexpected topic]"
- "The API returned articles from [unexpected source]"
- "Next time I would add NOT [term] to exclude..."

---

## Grading Summary

| Component | Points |
|-----------|--------|
| Part A: Q1-Q5 | 25 |
| Part B: Scenario 1 | 10 |
| Part B: Scenario 2 | 10 |
| Part B: Best practices | 5 |
| Part C: Task 1 | 15 |
| Part C: Task 2 | 10 |
| Part C: Task 3 | 15 |
| Part C: Task 4 | 10 |
| **TOTAL** | **100** |

---

## Bonus Question (5 extra points)

**Question:** What ethical considerations for social media data collection?

**Model Answer:**
> Researchers should: (1) comply with Terms of Service, (2) not collect PII without consent, (3) consider public vs. semi-private posts, (4) anonymize when publishing, (5) not overwhelm servers, (6) be transparent in publications, and (7) consider potential harms from identification.

**Rubric:** 1 point per valid consideration (max 5)

---

## Common Student Errors

1. **Keywords too broad**
   - Error: Using single word like "depression"
   - Fix: Combine with context terms using AND

2. **Forgetting rate limits**
   - Error: Getting blocked by API
   - Fix: Add time.sleep() between requests

3. **Not checking relevance**
   - Error: Analyzing garbage data
   - Fix: Always sample and inspect first

4. **Missing documentation**
   - Error: Can't reproduce collection
   - Fix: Log all parameters

5. **Not removing duplicates**
   - Error: Same article counted multiple times
   - Fix: `df.drop_duplicates()`

---

*Answer Key Version: 1.0 | Date: 2026-01-15*
