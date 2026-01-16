# Module 4 Assessment: Data Collection

**Exemplar Collections:** Elle (55 YouTube channels), Andrea (Reddit), Peter (News)
**Reference:** See DATASETS_FOR_M4.md for collection strategies and code examples

---

## Part A: Concept Check (25 points)

### Question 1 (5 points)
What is an API, and how does it differ from web scraping?

**Model Answer:** An API (Application Programming Interface) is a structured, official way to request data from a service—like placing an order at a restaurant. It's authorized, reliable, and returns data in a consistent format. Web scraping is extracting data directly from web pages, often without explicit permission. APIs are preferred because they're more reliable, ethical, and less likely to break when websites change.

---

### Question 2 (5 points)
Why might the keyword "anxiety" return irrelevant results when studying mental health?

**Model Answer:** "Anxiety" is too broad and has multiple meanings beyond mental health: stock market anxiety, anxiety about sports outcomes, movie titles, etc. Without additional context or filtering, you'll get a mix of content that doesn't relate to psychological anxiety, making your dataset noisy and reducing validity.

---

### Question 3 (5 points)
What is a rate limit, and how should you handle it?

- A) A limit on how much data you can download total; ignore it
- B) A limit on requests per time period; add delays between requests
- C) A limit on file size; compress your data
- D) A limit on keywords; use fewer search terms

**Correct Answer:** B

---

### Question 4 (5 points)
Why is it important to inspect your data BEFORE running analysis?

**Model Answer:** To ensure data quality and relevance. Without inspection, you might analyze irrelevant articles (garbage in, garbage out), miss duplicates that skew results, or not notice missing values. A quick quality check catches problems early when they're easier to fix—either by refining keywords or cleaning the data.

---

### Question 5 (5 points)
What information should you document about your data collection process for the Methods section?

**Model Answer:** You should document: (1) the API/source used, (2) exact keywords and search query, (3) date range, (4) any filters applied (language, source type), (5) total number of results collected, (6) when collection occurred, and (7) any cleaning steps performed. This enables reproducibility.

---

## Part B: Keyword Design (25 points)

### Scenario 1 (10 points)
You want to study public reaction to AI replacing jobs.

**Current keyword:** `AI`

**Problems with this keyword:** (List 2)
1. _______________________
2. _______________________

**Improved keyword query:**
_______________________

**Model Answer:**
Problems:
1. "AI" alone will return results about artificial intelligence in general (research, products, etc.), not specifically about job displacement
2. It will also return false positives like "AI" as part of company names or unrelated acronyms

Improved query: `"artificial intelligence" AND (jobs OR employment OR workers OR unemployment OR "job loss" OR automation)`

---

### Scenario 2 (10 points)
You want to study social media's effect on teen mental health.

Design a keyword query using AND/OR operators:

**Your query:**
_______________________

**What filters would you apply?**
- Date range: _______________________
- Language: _______________________
- Other: _______________________

**Model Answer:**
Query: `("social media" OR Instagram OR TikTok OR Snapchat) AND (teen OR adolescent OR youth) AND ("mental health" OR depression OR anxiety OR wellbeing)`

Filters:
- Date range: 2020-01-01 to present (recent coverage, post-pandemic)
- Language: English
- Other: Exclude sources that are primarily marketing/promotional

---

### Keyword Best Practices (5 points)
List 3 best practices for keyword selection:

1. _______________________
2. _______________________
3. _______________________

**Model Answer:**
1. Use specific phrases in quotes when looking for exact matches
2. Use AND to require multiple concepts, OR to expand alternatives
3. Test with a small sample first to check relevance before full collection

---

## Part C: Lab Results (50 points)

### Task 1: Collection Summary (15 points)

Complete your data collection log:

| Field | Your Value |
|-------|------------|
| Topic chosen | |
| Keywords used | |
| Date range | |
| API/Source | |
| Articles requested | |
| Articles received | |
| Unique articles (after dedup) | |

---

### Task 2: Data Preview (10 points)

Submit a screenshot showing:
- [ ] First 5 rows of your data (3 points)
- [ ] Column names visible (2 points)
- [ ] Total row count visible (2 points)
- [ ] At least title and source columns shown (3 points)

---

### Task 3: Quality Assessment (15 points)

**Relevance Check:**
You read 10 random samples from your data.

How many were relevant to your topic? _____ / 10

If relevance was below 7/10, what changes would improve it?
_______________________

---

**Duplicate Check:**
How many duplicates did you remove? _____

---

**Date Range Check:**
- Earliest article date: _______
- Latest article date: _______
- Is this within your expected range? Yes / No

---

### Task 4: Reflection (10 points)

In 3-4 sentences, reflect on the data collection process:
1. What was challenging about selecting keywords?
2. Were there any surprises in what the API returned?
3. How might you refine your approach if doing this again?

---

## Grading Summary

| Component | Points |
|-----------|--------|
| Part A: Concept Check | 25 |
| Part B: Keyword Design | 25 |
| Part C: Lab Results | 50 |
| **Total** | **100** |

---

## Submission Instructions

1. Complete all sections in a single document
2. Include screenshots where requested
3. Upload your CSV file to the course platform
4. Submit via [Course Platform] by [Deadline]

---

## Bonus Question (5 extra points)

What ethical considerations should researchers keep in mind when collecting data from social media APIs?

**Model Answer:** Researchers should: (1) comply with platform Terms of Service, (2) not collect private or personally identifiable information without consent, (3) consider whether posts were intended to be public vs. semi-private, (4) anonymize data when publishing, (5) not overwhelm servers with requests, (6) be transparent about data collection methods in publications, and (7) consider potential harms if the collected data could identify or embarrass individuals.
