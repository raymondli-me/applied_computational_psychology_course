# Module 1 Flashcards: The Dataset & The Question

**Total Cards:** 22
**Format:** Anki-compatible (Front/Back)

---

## Definitions (7 cards)

### Card 1
**Front:** What is an observation in a dataset?
**Back:** A single row in a dataset - one "thing" being studied. Example: one YouTube comment, one Reddit post, one video.
**Tags:** M1, definition, tidy_data

### Card 2
**Front:** What is a variable in a dataset?
**Back:** A column in a dataset - something measured about each observation. Example: like_count, comment_text, view_count.
**Tags:** M1, definition, tidy_data

### Card 3
**Front:** What is structured data?
**Back:** Data already organized in rows and columns with defined types (numbers, categories, dates). Example: view_count = 1500.
**Tags:** M1, definition, data_types

### Card 4
**Front:** What is unstructured data?
**Back:** Raw content without predefined format - text, images, audio. Example: "This video changed my life, thank you so much!"
**Tags:** M1, definition, data_types

### Card 5
**Front:** What is the independent variable (IV)?
**Back:** The variable you predict FROM - the potential cause or input. It's the X in "X predicts Y."
**Tags:** M1, definition, hypothesis

### Card 6
**Front:** What is the dependent variable (DV)?
**Back:** The variable you predict - the outcome or output. It's the Y in "X predicts Y."
**Tags:** M1, definition, hypothesis

### Card 7
**Front:** What is NaN in data?
**Back:** "Not a Number" - represents missing data. Also appears as N/A, null, None, blank cells.
**Tags:** M1, definition, data_cleaning

---

## Concepts (7 cards)

### Card 8
**Front:** What are the three rules of Tidy Data (Hadley Wickham)?
**Back:** 1. Every column is ONE variable. 2. Every row is ONE observation. 3. Every cell contains ONE value.
**Tags:** M1, concept, tidy_data

### Card 9
**Front:** Why is tidy data important?
**Back:** It makes analysis possible. Once data is tidy (rows = observations, columns = variables), you can do math on human behavior - calculate means, run regressions, etc.
**Tags:** M1, concept, tidy_data

### Card 10
**Front:** What's wrong with "depression, anxiety, therapy" in one cell?
**Back:** Violates tidy data rule #3 (one value per cell). You can't easily count how many videos mention "anxiety" when it's buried with other values. Split into separate columns or rows.
**Tags:** M1, concept, tidy_data

### Card 11
**Front:** How can unstructured data be converted to structured data?
**Back:** Three methods: 1) Human raters code it (e.g., rate conflict severity 1-7). 2) LLMs rate it (Module 3). 3) Count/extract features (word count, keywords).
**Tags:** M1, concept, data_types

### Card 12
**Front:** Why must hypotheses be directional?
**Back:** "Relates to" isn't testable. You need "increases" or "decreases" to make a specific prediction that can be confirmed or refuted. Example: "Longer comments will receive MORE likes."
**Tags:** M1, concept, hypothesis

### Card 13
**Front:** What's the difference between correlation and causation?
**Back:** Correlation: X and Y move together. Causation: X makes Y happen. Just because word count predicts likes doesn't mean typing more CAUSES more likes. Need experiments for causation.
**Tags:** M1, concept, hypothesis

### Card 14
**Front:** Why inspect data BEFORE analysis?
**Back:** Garbage in, garbage out. Catch missing values, duplicates, wrong formats, irrelevant content early when they're easier to fix. 5 minutes of inspection saves hours of debugging.
**Tags:** M1, concept, data_cleaning

---

## Code Patterns (5 cards)

### Card 15
**Front:** How do you load a course dataset in Python?
**Back:**
```python
df = load_dataset("dataset_name", nrows=5000)
print(f"Loaded {len(df)} rows")
print(df.columns)
```
**Tags:** M1, code, data_loading

### Card 16
**Front:** How do you see the first few rows of a DataFrame?
**Back:**
```python
df.head()  # First 5 rows
df.head(10)  # First 10 rows
```
**Tags:** M1, code, data_exploration

### Card 17
**Front:** How do you get basic statistics for a DataFrame?
**Back:**
```python
df.describe()  # Count, mean, std, min, max for numeric columns
df.info()  # Column types, non-null counts
```
**Tags:** M1, code, data_exploration

### Card 18
**Front:** How do you check for missing values in Python?
**Back:**
```python
df.isna().sum()  # Count NaN per column
df.dropna()  # Remove rows with any NaN
df.fillna(0)  # Replace NaN with 0
```
**Tags:** M1, code, data_cleaning

### Card 19
**Front:** How do you remove duplicate rows?
**Back:**
```python
df.drop_duplicates()  # Remove exact duplicates
df.drop_duplicates(subset=['post_id', 'text'])  # Check specific columns
```
**Tags:** M1, code, data_cleaning

---

## Interpretation (2 cards)

### Card 20
**Front:** A dataset has 10,000 rows and 15 columns. What does this mean?
**Back:** 10,000 observations (e.g., 10,000 comments/posts/videos) and 15 variables measured for each one (e.g., like_count, text, date, author).
**Tags:** M1, interpretation, tidy_data

### Card 21
**Front:** Your data shows 500 missing values in "author_name" but 0 missing in "comment_text". What do you do?
**Back:** Keep going - author_name is non-critical. The critical column (comment_text) has no missing data. Document the missingness but don't delete rows unless critical data is missing.
**Tags:** M1, interpretation, data_cleaning

---

## Common Mistakes (1 card)

### Card 22
**Front:** What's wrong with: "We predict that self-disclosure relates to support"?
**Back:** No direction. Should be: "We predict that videos WITH self-disclosure will have HIGHER support ratings." Always specify increase/decrease.
**Tags:** M1, mistake, hypothesis

---

*Module 1 Flashcards | Applied Psychological Data Science*
