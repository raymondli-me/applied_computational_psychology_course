# Module 1 Answer Key: Data Foundations
## INSTRUCTOR USE ONLY

**Assessment:** Module 1 Assessment
**Dataset:** `andrea_sample_2k_for_sheets` (2,000 row sample in Google Sheets)
**Total Points:** 100

---

## Part A: Concept Check (30 points)

### Question 1 (10 points)
**Question:** In a tidy dataset, what do rows and columns represent?

**Correct Answer:** B) Rows = observations, Columns = variables

**Rubric:**
| Score | Criteria |
|-------|----------|
| 10 | Selects B |
| 0 | Any other answer |

**Common Errors:**
- Confusing A and B (rows/columns reversed)
- Selecting C (headers vs variables confusion)

---

### Question 2 (10 points)
**Question:** Which of the following is an example of UNTIDY data?

**Correct Answer:** B) A spreadsheet where "view_count, like_count" are stored in the same column as different rows

**Rubric:**
| Score | Criteria |
|-------|----------|
| 10 | Selects B |
| 0 | Any other answer |

**Instructor Note:** Option B violates tidy data principles because it combines multiple variable types in one column. Students who select D may think "no missing values" makes data tidy - clarify that tidiness is about structure, not completeness.

---

### Question 3 (10 points)
**Question:** What is the difference between structured and unstructured data?

**Model Answer:**
> Structured data is already organized into rows and columns with defined types (like CSVs with numerical or categorical values). Unstructured data is raw content like text, images, or audio that doesn't have a pre-defined format. Example: A "view_count" column is structured; a "comment_text" column is unstructured.

**Rubric:**
| Score | Criteria |
|-------|----------|
| 10 | Full credit: Correct definition of both, clear example |
| 8 | Definitions correct but example unclear |
| 6 | One definition correct with example |
| 4 | Partial understanding of distinction |
| 2 | Vague attempt at distinction |
| 0 | No attempt or completely incorrect |

**Key Terms Expected:**
- Structured: organized, defined format, rows/columns, numerical, categorical
- Unstructured: raw, no predefined format, text/images/audio

---

## Part B: Practical Application (50 points)

### Task 1: Data Cleaning Screenshot (25 points)

**Checklist:**
| Requirement | Points | What to Look For |
|-------------|--------|------------------|
| Standardized column headers | 5 | No spaces, lowercase, consistent naming |
| First 20 rows visible | 5 | Screenshot shows enough data |
| No NaN in critical columns | 10 | Post Title, Post Score should be clean |
| Row count showing dedup | 5 | Should see info about duplicate removal |

**Expected Data Info (for reference):**
```
Sample dataset: 2,000 rows x 16 columns (in Google Sheets)
Columns: Post Title, Post URL, Post Score, Post Author, Post Num Comments,
         Post Body, Media URL, Post Created, Comment Body, Comment Author,
         Comment Score, Comment Created, Reply Body, Reply Author,
         Reply Score, Reply Created
```

---

### Task 2: Variable Classification (15 points)

**Correct Answers:**

| Variable | Type | Rationale |
|----------|------|-----------|
| Post URL | Nominal/Categorical | Unique identifier, no numerical ordering; used for identification only |
| Post Body | Unstructured Text | Raw text content requiring transformation for analysis; no predefined categories |
| Post Score | Continuous/Interval | Numerical value that can be negative; measures engagement |
| Post Num Comments | Continuous/Ratio | Count data with a true zero; represents engagement level |
| Comment Body | Unstructured Text | Raw text content requiring transformation; qualitative data |

**Rubric:**
- Correct type identification: 2 points each (10 total)
- Clear rationale: 1 point each (5 total)

**Acceptable Type Answers:**
| Variable | Acceptable Answers |
|----------|-------------------|
| Post URL | Nominal, Categorical, String, ID |
| Post Body | Unstructured, Text, String, Qualitative |
| Post Score | Continuous, Interval, Ratio, Numerical, Integer |
| Post Num Comments | Continuous, Ratio, Count, Discrete, Integer |
| Comment Body | Unstructured, Text, String, Qualitative |

**Note on Subreddit:** The dataset doesn't have a subreddit column directly, but students can derive it:
```python
df['subreddit'] = df['Post URL'].str.extract(r'/r/([^/]+)/')
```

---

### Task 3: Hypothesis Formation (10 points)

**Template:** "We predict that [IV] will [direction] [DV]"

**Exemplar Hypotheses:**
1. "We predict that post length (IV) will increase post score (DV)"
2. "We predict that comment score (IV) will increase with post score (DV)"
3. "We predict that number of comments (IV) will increase post score (DV)"

**Rubric:**
| Score | Criteria |
|-------|----------|
| 10 | Perfect: Clear IV/DV, directional prediction, uses actual dataset variables |
| 8 | Good: Minor issue (e.g., direction unclear but IV/DV correct) |
| 6 | Acceptable: Testable but vague (e.g., "relates to" instead of direction) |
| 4 | Needs work: Missing IV or DV identification |
| 2 | Incomplete: Not testable or uses made-up variables |
| 0 | Not submitted |

**Valid Variables from Dataset:**
- Post Score, Post Num Comments, Comment Score, Reply Score (numerical)
- Post Body length, Comment Body length (derived)

**Invalid Hypotheses (examples):**
- "Posts with more likes will be popular" (no "likes" column)
- "Reddit posts will have engagement" (no direction, vague)
- "Post Score affects Comment Score" (reverse causality implied)

---

## Part C: Reflection (20 points)

### Question 4 (10 points)
**Question:** Describe ONE challenge encountered while cleaning data and how you solved it.

**Model Answer:**
> "I found that some rows had 'nan' in lowercase while others had 'NaN' with capital letters. The Find & Replace function only caught one version at first. I solved this by running Find & Replace twice with both versions."

**Rubric:**
| Score | Criteria |
|-------|----------|
| 10 | Specific challenge identified, clear solution described |
| 7 | Challenge identified but solution vague |
| 4 | Vague challenge, partial solution |
| 2 | Mentioned cleaning without specifics |
| 0 | No attempt |

**Common Challenges Students May Mention:**
- Duplicate rows
- Missing values (NaN, null, empty strings)
- Inconsistent date formats
- Unicode characters in text
- Very long text fields
- Column name inconsistencies

---

### Question 5 (10 points)
**Question:** Identify ONE unstructured and ONE structured column, and how to transform unstructured to structured.

**Model Answer:**
> The `Post Body` column contains unstructured data (raw post text), while `Post Score` contains structured data (numerical upvotes). To transform `Post Body` into structured data, you could: (1) have raters code the conflict type (in-laws, venue, budget), (2) use an LLM to rate emotional intensity on a 1-7 scale, or (3) count specific keywords related to the research question.

**Rubric:**
| Score | Criteria |
|-------|----------|
| 10 | Correct identification of both types + creative transformation method |
| 8 | Both types correct, transformation method unclear |
| 6 | One type correct, transformation attempt |
| 4 | Types confused but transformation reasonable |
| 2 | Vague attempt |
| 0 | No attempt |

**Valid Structured Columns:** Post Score, Post Num Comments, Comment Score, Reply Score
**Valid Unstructured Columns:** Post Body, Comment Body, Reply Body, Post Title

**Valid Transformation Methods:**
- Human coding/rating
- LLM rating
- Keyword counting
- Sentiment analysis
- Character/word counting
- Topic modeling
- Named entity extraction

---

## Grading Summary

| Component | Points |
|-----------|--------|
| Part A: Q1 (MC) | 10 |
| Part A: Q2 (MC) | 10 |
| Part A: Q3 (Short Answer) | 10 |
| Part B: Task 1 (Screenshot) | 25 |
| Part B: Task 2 (Classification) | 15 |
| Part B: Task 3 (Hypothesis) | 10 |
| Part C: Q4 (Reflection) | 10 |
| Part C: Q5 (Transform) | 10 |
| **TOTAL** | **100** |

---

## Expected Google Sheets Output Reference

When students load the data via IMPORTDATA:
```
=IMPORTDATA("https://storage.googleapis.com/.../andrea_sample_2k_for_sheets.csv")
```

**Expected Result:**
- 2,000 rows loaded
- 16 columns visible
- Column headers in row 1

**Note:** Module 1 uses Google Sheets only. Python/Colab starts in Module 2.

---

*Answer Key Version: 1.0 | Date: 2026-01-15*
