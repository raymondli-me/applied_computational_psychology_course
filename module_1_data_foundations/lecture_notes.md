# Module 1: Lecture Script
## "From Comments to Conclusions: The Data Journey"

**Total Runtime:** ~35 minutes
**Video Production Ready:** Yes

---

### INTRO [0:00-2:00]
*[INSTRUCTOR NOTE: Start with energy - this sets the tone for the course]*

**[SLIDE: Andrea's Reddit Data - 871,000 posts]**

*"Eight hundred seventy-one thousand Reddit posts. Fifteen research assistants. Eight hundred twenty-five datasets. One course that teaches you how to analyze them all."*

*"Andrea collected nearly a million posts about wedding conflicts. Peter scraped 765,000 news videos from Fox and MSNBC. Kaitlyn organized 809,000 YouTube comments about mental health. These are REAL datasets from REAL researchers who sat exactly where you're sitting now."*

*"By the end of this course, you'll be able to work with any of them. Not by reading every post yourself—that would take years—but by teaching a computer to read them for you."*

*"But before we get to the fancy AI stuff, we need to master the fundamentals. Today's topic: What even IS data?"*

---

### SECTION 1: THE ANATOMY OF A DATASET [2:00-10:00]
*[INSTRUCTOR NOTE: Use visual hand gestures when pointing to rows vs columns]*

**[SLIDE: Image of a spreadsheet with highlighted rows and columns]**

*"Look at this spreadsheet. It seems simple, right? Rows and columns. But understanding the logic behind this structure is the foundation of everything we'll do."*

**[CLICK: Highlight rows]**

*"Each row is an OBSERVATION. In the RA Manuscript, an observation might be a single YouTube video or a single comment. Think of it as one 'thing' you're studying."*

**[CLICK: Highlight columns]**

*"Each column is a VARIABLE. That's something you MEASURED about each observation. View count. Word count. Whether someone disclosed their diagnosis."*

*"Here's the key insight: The power of quantitative research is that once your data looks like this—neat rows and columns—you can do MATH on human behavior."*

**[SLIDE: Messy data example]**

*"But real-world data doesn't come to you clean. It looks like THIS. Missing values everywhere. Duplicate entries. Column headers that say 'untitled1'. Your first job as a computational researcher? Cleaning house."*

---

### SECTION 2: TIDY DATA PRINCIPLES [10:00-18:00]
*[INSTRUCTOR NOTE: This is core material - slow down and ensure understanding]*

**[SLIDE: Hadley Wickham's Tidy Data visual]**

*"Computer scientist Hadley Wickham coined the term 'Tidy Data.' Three rules:"*

1. *"Every column is ONE variable"*
2. *"Every row is ONE observation"*
3. *"Every cell contains ONE value"*

*"Sounds obvious? Let me show you what UNTIDY data looks like."*

**[SLIDE: Untidy example - multiple values per cell]**

*"See this? 'Tags' column with 'depression, anxiety, therapy' all crammed into one cell. That's untidy. You can't easily count how many videos mention 'anxiety' when it's buried with other tags."*

**[SLIDE: Untidy example - variables as rows]**

*"Or this—someone stored different metrics in rows instead of columns. Now 'view_count' and 'like_count' are in the same column. How do you calculate their correlation? You can't, not easily."*

*"Your mantra: Before ANY analysis, make your data TIDY."*

---

### SECTION 3: STRUCTURED VS. UNSTRUCTURED DATA [18:00-25:00]
*[INSTRUCTOR NOTE: The "magic" revelation - this is the hook for the rest of the course]*

**[SLIDE: Two-panel comparison]**

*"There's one more distinction we need to make: structured versus unstructured data."*

**[LEFT PANEL: CSV file]**

*"This is STRUCTURED data. It's already in that nice rows-and-columns format. View counts. Dates. Categories. Computers love this."*

**[RIGHT PANEL: Raw comment text]**

*"This is UNSTRUCTURED data. A wall of text. A comment that says 'This video literally saved my life, I was in such a dark place last year.' Beautiful, human, messy."*

*"Here's the magic of modern computational psychology: We can CONVERT unstructured data INTO structured data. That comment? An AI can read it and output: 'Support level: 7/7. Self-disclosure: Yes.'"*

*"We'll learn exactly how to do that in Module 3. For now, just know: both types of data are valuable. We need both."*

---

### SECTION 4: FORMULATING A HYPOTHESIS [25:00-30:00]
*[PAUSE: Check for understanding before moving on]*

**[SLIDE: Hypothesis formula]**

*"Now let's talk about the QUESTION. Before you touch any data, you need a hypothesis. A prediction."*

*"The formula:"*

> **"We predict that [INDEPENDENT VARIABLE] will [increase/decrease] [DEPENDENT VARIABLE]"**

*"From the RA Manuscript: 'We predict that videos featuring self-disclosure will have higher support ratings in the comments.'"*

- *Independent Variable (IV): Self-disclosure (yes/no)*
- *Dependent Variable (DV): Support rating (1-7 scale)*

*"Notice: the IV is something that varies naturally or that you manipulate. The DV is what you measure as an outcome. The IV predicts; the DV gets predicted."*

**[SLIDE: Bad hypothesis examples]**

*"Common mistakes:"*
- *Too vague: 'Mental health videos are interesting' — not testable*
- *No variables: 'People like YouTube' — what are you measuring?*
- *No direction: 'Self-disclosure relates to support' — up or down?*

---

### WRAP-UP [30:00-32:00]

**[SLIDE: Today's Takeaways]**

*"Three things to remember:"*

1. *"Data = Rows (observations) + Columns (variables)"*
2. *"Tidy your data BEFORE analysis"*
3. *"Every study starts with a testable hypothesis: IV predicts DV"*

*"In today's lab, you'll get your hands dirty with real messy data. You'll clean it up, and you'll write your first hypothesis. This is where real research begins."*

*"See you in the lab."*

---

### SECTION 5: ACCESSING COURSE DATASETS [32:00-35:00]
*[LIVE CODING: Share screen, have students follow along if possible]*

**[SLIDE: The Course Dataset Bank]**

*"In this course, you'll work with 825 datasets contributed by past research assistants. Here's how to access them."*

**[LIVE DEMO: Colab notebook]**

```python
# Load the course data catalog
import pandas as pd, json, urllib.request
GCS_BUCKET = "variable-resolution-applied-computational-psychology-course"
CATALOG_URL = f"https://storage.googleapis.com/{GCS_BUCKET}/manifest.json"

# Load any dataset with one line
df = load_dataset("andrea_reddit_results_andrea_2025_03_13", nrows=5000)
print(f"Loaded {len(df):,} rows from Andrea's wedding Reddit research")
print(f"Columns: {list(df.columns)}")
# Key columns: Post Title, Post URL, Post Score, Post Body, Post Num Comments
```

*"That's it. One line, 871,000 rows. In your lab today, you'll explore Andrea's dataset and formulate your first hypothesis."*

*"Every dataset in this course has a story. Andrea wanted to understand wedding conflicts. Peter studied political media. Kaitlyn explored mental health support. You'll learn their methods as you work with their data."*

---

### LECTURE MATERIALS CHECKLIST
- [ ] Course Dataset Bank demo (Colab)
- [ ] Slide deck with real dataset examples (Andrea, Peter, Kaitlyn)
- [ ] Messy CSV file for demo
- [ ] Tidy Data visual from Wickham's paper
- [ ] DATASETS_FOR_M1.md reference card
