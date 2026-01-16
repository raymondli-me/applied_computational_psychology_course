# Module 1 Assessment: Data Foundations

**Recommended Dataset:** `andrea_reddit_results_andrea_2025_03_13` (Andrea's Wedding Reddit)
**Alternate Datasets:** See DATASETS_FOR_M1.md for other options

---

## Part A: Concept Check (30 points)

### Question 1 (10 points)
In a tidy dataset, what do rows and columns represent?

- A) Rows = variables, Columns = observations
- B) Rows = observations, Columns = variables
- C) Rows = data, Columns = headers
- D) Rows = independent variables, Columns = dependent variables

**Correct Answer:** B

---

### Question 2 (10 points)
Which of the following is an example of UNTIDY data?

- A) A spreadsheet with one measurement per cell
- B) A spreadsheet where "view_count, like_count" are stored in the same column as different rows
- C) A spreadsheet with unique column headers
- D) A spreadsheet with no missing values

**Correct Answer:** B

---

### Question 3 (10 points)
What is the difference between structured and unstructured data?

**Model Answer:**
Structured data is already organized into rows and columns with defined types (like CSVs with numerical or categorical values). Unstructured data is raw content like text, images, or audio that doesn't have a pre-defined format. Example: A "view_count" column is structured; a "comment_text" column is unstructured.

---

## Part B: Practical Application (50 points)

### Task 1: Data Cleaning Screenshot (25 points)

Submit a screenshot of your cleaned dataset showing:
- [ ] Standardized column headers (5 points)
- [ ] First 20 rows of data visible (5 points)
- [ ] No visible NaN or missing values in critical columns (10 points)
- [ ] Row count visible showing duplicates were removed (5 points)

---

### Task 2: Variable Classification (15 points)

Using Andrea's Reddit dataset (`andrea_reddit_results_andrea_2025_03_13`), complete the table:

| Variable | Type | Rationale |
|----------|------|-----------|
| Post URL | _____ | _____ |
| Post Body | _____ | _____ |
| Post Score | _____ | _____ |
| Post Num Comments | _____ | _____ |
| Comment Body | _____ | _____ |

*Note: To get subreddit, extract from Post URL: `df['subreddit'] = df['Post URL'].str.extract(r'/r/([^/]+)/')`*

**Grading:**
- Correct type identification (2 points each)
- Clear rationale (3 points each)

---

### Task 3: Hypothesis Formation (10 points)

Write a testable hypothesis using the template:

> "We predict that [IV] will [direction] [DV]"

**Requirements:**
- Uses variables available in the dataset (3 points)
- Specifies a clear direction (increase/decrease) (3 points)
- IV and DV are correctly identified (4 points)

---

## Part C: Reflection (20 points)

### Question 4 (10 points)
In 2-3 sentences, describe ONE challenge you encountered while cleaning the data and how you solved it.

**Example Good Answer:**
"I found that some rows had 'nan' in lowercase while others had 'NaN' with capital letters. The Find & Replace function only caught one version at first. I solved this by running Find & Replace twice with both versions."

---

### Question 5 (10 points)
Looking at Andrea's Reddit dataset, identify ONE column that contains unstructured data and ONE column that contains structured data. How might you transform the unstructured column into structured data for analysis?

**Model Answer:**
The `Post Body` column contains unstructured data (raw post text), while `Post Score` contains structured data (numerical upvotes). To transform `Post Body` into structured data, you could: (1) have raters code the conflict type (in-laws, venue, budget), (2) use an LLM to rate emotional intensity on a 1-7 scale, or (3) count specific keywords related to the research question.

---

## Grading Summary

| Component | Points |
|-----------|--------|
| Part A: Concept Check | 30 |
| Part B: Practical Application | 50 |
| Part C: Reflection | 20 |
| **Total** | **100** |

---

## Submission Instructions

1. Export your cleaned Google Sheet as a PDF or share link
2. Submit your written answers (Questions 1-5) as a single document
3. Include all screenshots with clear labels
4. Submit via [Course Platform] by [Deadline]

---

## Rubric for Hypothesis (Detailed)

| Score | Description |
|-------|-------------|
| 10 | Perfect: Clear IV/DV, directional prediction, uses dataset variables |
| 8 | Good: Minor issue (e.g., direction unclear but IV/DV correct) |
| 6 | Acceptable: Testable but vague (e.g., "relates to" instead of direction) |
| 4 | Needs work: Missing IV or DV identification |
| 2 | Incomplete: Not testable or doesn't use dataset |
| 0 | Not submitted |
